"""Encoders configuration.

Attributes starting with '_' are seen by the user as read only options.

"""

import subprocess
import shutil
import logging

from .upnp.util import NL_INDENT

DEFAULT_SELECTION = (
    'Mp3Encoder',
    'FFMpegMp3Encoder',

    # Lossless encoders.
    'L16Encoder',
    'FFMpegL16WavEncoder',
    'FFMpegAiffEncoder',
    'FlacEncoder',
    'FFMpegFlacEncoder',

    # Lossy encoders.
    'FFMpegOpusEncoder',
    'FFMpegVorbisEncoder',
    'FFMpegAacEncoder',
)

def select_encoder(config, renderer_name, pinfo, udn):
    """Select the encoder.

    Return the selected encoder instance, the mime type and protocol info.
    """

    logger = logging.getLogger('encoder')

    def found_encoder(encoder, proto):
        if encoder.has_mime_type(proto[2]):
            logger.info(f"Selected encoder mime type: '{encoder.mime_type}'")
            return encoder, encoder.mime_type, ':'.join(proto)

    # The ProtocolInfo format is:
    #   <protocol>“:”<network>“:”<contentFormat>“:”<additionalInfo>
    # We are interested in the HTTP streaming entries:
    #   http-get:*:mime-type:*
    protocol_infos = [proto.split(':') for proto in
                            (x.strip() for x in pinfo['Sink'].split(',')) if
                      proto.startswith('http-get:')]
    mime_types = [proto[2] for proto in protocol_infos]
    logger.debug(f'{renderer_name} renderer mime types:' + NL_INDENT +
                 f'{mime_types}')

    # Try first the configured udns.
    for section, encoder in config.udns.items():
        if section == udn:
            # Check that the list of mime_types holds one of the  mime types
            # supported by this encoder.
            for proto in protocol_infos:
                result = found_encoder(encoder, proto)
                if result is not None:
                    return result
            else:
                logger.error(f'No matching mime type for the udn configured'
                             f' on the {encoder} encoder')
                return None

    # Then the encoders proper.
    for encoder in config.encoders.values():
        for proto in protocol_infos:
            result = found_encoder(encoder, proto)
            if result is not None:
                return result

class Encoder:
    """The pa-dlna default configuration.

    This is the built-in pa-dlna configuration written as text. It can be
    parsed by a Python Configuration parser and consists of sections, each led
    by a [section] header, followed by option/value entries separated by
    '='. See https://docs.python.org/3/library/configparser.html.

    The 'selection' option is written as a multi-line in which case all the
    lines after the first line start with a white space.

    The default value of 'selection' lists the encoders in this order:
        - mp3 encoders first as mp3 is the most common encoding
        - lossless encoders
        - then lossy encoders
    See https://trac.ffmpeg.org/wiki/Encode/HighQualityAudio.
    """

    def __init__(self):
        self.selection = DEFAULT_SELECTION
        self.sample_format = 's16le'
        self.rate = 44100
        self.channels = 2
        self.track_metadata = True
        self.soap_minimum_interval = 5
        self.args = None

    @property
    def available(self):
        if hasattr(self, '_available'):
            return self._available
        return True

    @property
    def mime_type(self):
        assert hasattr(self, 'requested_mtype')
        return self.requested_mtype

    def has_mime_type(self, mime_type):
        if mime_type.lower().strip() in self._mime_types:
            self.requested_mtype = mime_type
            return True

    def set_args(self):
        raise NotImplementedError

    @property
    def command(self):
        if hasattr(self, '_command'):
            return self._command
        elif hasattr(self, '_pgm'):
            cmd = [self._pgm]
            cmd.extend(self.args.split())
            return cmd

    @command.setter
    def command(self, value):
        """The command setter used by the test suite."""
        self._command = value

    def __str__(self):
        return self.__class__.__name__

ROOT_ENCODER = Encoder

class StandAloneEncoder(Encoder):
    """Abstract class for standalone encoders."""

    def __init__(self):
        super().__init__()

class L16Mixin():
    """Mixin class for L16 encoders."""

    @property
    def mime_type(self):
        assert hasattr(self, 'requested_mtype')
        return self.requested_mtype

    def has_mime_type(self, mime_type):
        # For example 'audio/L16;rate=44100;channels=2'.
        mtype = [p.strip() for p in mime_type.lower().split(';')]

        if mtype[0] != self._mime_types[0]:
            return False

        rate_channels = [None, None]            # list of [rate, channels]
        for param in mtype[1:]:
            for (n, prefix) in enumerate(['rate=', 'channels=']):
                if param.startswith(prefix):
                    try:
                        rate_channels[n] = int(param[len(prefix):])
                    except ValueError:
                        return False
                    break

        if (rate_channels[0] not in (None, self.rate) or
                rate_channels[1] not in (None, self.channels)):
            return False

        if rate_channels[0] is None:
            # The DLNA answer to GetProtocolInfo includes 'audio/L16' without
            # the rate which is required in the 'Content-type' field of the
            # HTTP '200 OK' response sent to the DLNA.
            mime_type = f'{mime_type};rate={self.rate}'

        if rate_channels[1] is None:
            mime_type = f'{mime_type};channels={self.channels}'

        self.requested_mtype = mime_type
        return True

class FlacEncoder(StandAloneEncoder):
    """Lossless Flac encoder.

    See the flac home page at https://xiph.org/flac/
    See also https://xiph.org/flac/documentation_tools_flac.html
    """

    def __init__(self):
        self._pgm = shutil.which('flac')
        self._available = self._pgm is not None
        self._mime_types = ['audio/flac', 'audio/x-flac']
        super().__init__()

    def set_args(self):
        endian = 'little' if self.sample_format == 's16le' else 'big'
        self.args = (f'- --silent --channels {self.channels} '
                     f'--sample-rate {self.rate} '
                     f'--sign signed --bps 16 --endian {endian}')

class L16Encoder(L16Mixin, StandAloneEncoder):
    """Lossless PCM L16 encoder without a container.

    This encoder does not use an external program for streaming. It only uses
    the Pulseaudio parec program.
    See also https://datatracker.ietf.org/doc/html/rfc2586.
    """

    def __init__(self):
        self._mime_types = ['audio/l16']
        StandAloneEncoder.__init__(self)
        self.sample_format = 's16be'

    def set_args(self):
        pass

class Mp3Encoder(StandAloneEncoder):
    """Mp3 encoder from the Lame Project.

    See the Lame Project home page at https://lame.sourceforge.io/
    See lame command line options at
        https://svn.code.sf.net/p/lame/svn/trunk/lame/USAGE
    """

    def __init__(self):
        self._pgm = shutil.which('lame')
        self._available = self._pgm is not None
        self._mime_types = ['audio/mp3', 'audio/mpeg']
        super().__init__()
        self.bitrate = 256
        self.quality = 0

    def set_args(self):
        sampling = self.rate / 1000
        endian = 'little' if self.sample_format == 's16le' else 'big'
        self.args = (f'-r -s {sampling} --signed --bitwidth 16 '
                     f'--{endian}-endian '
                     f'-q {self.quality} -b {self.bitrate} -')


class FFMpegEncoder(Encoder):
    """Abstract class for ffmpeg encoders.

    See also https://www.ffmpeg.org/ffmpeg.html.
    """

    PGM = None
    FORMATS = None
    ENCODERS = None
    container = None
    encoder = None

    def __init__(self, mime_types, *, sample_format=None):
        assert self.container is not None

        if self.FORMATS is None:
            FFMpegEncoder.FORMATS = ''
            FFMpegEncoder.PGM = shutil.which('ffmpeg')
            if self.PGM is not None:
                proc = subprocess.run([self.PGM, '-formats'],
                                      stdout=subprocess.PIPE,
                                      stderr=subprocess.DEVNULL, text=True)
                FFMpegEncoder.FORMATS = proc.stdout
        self._available = self.container in self.FORMATS
        self._pgm = self.PGM
        self._mime_types = mime_types
        # End of setting options as comments.

        super().__init__()

        # Override the default sample_format.
        if sample_format is not None:
            self.sample_format = sample_format

        if self.encoder is not None:
            if self.ENCODERS is None:
                FFMpegEncoder.ENCODERS = ''
                if self.PGM is not None:
                    proc = subprocess.run([self.PGM, '-encoders'],
                                          stdout=subprocess.PIPE,
                                          stderr=subprocess.DEVNULL,
                                          text=True)
                    FFMpegEncoder.ENCODERS = proc.stdout
            self._available = self.encoder in self.ENCODERS and self._available

    def extra_args(self):
        return ''

    def set_args(self):
        self.args = (f'-loglevel error -hide_banner -nostats '
                     f'-ac {self.channels} -ar {self.rate} '
                     f'-f {self.sample_format} -i - '
                     f'-f {self.container}')
        if self.encoder is not None:
            self.args += f' -c:a {self.encoder}'
        extra = self.extra_args()
        if extra:
            self.args += f' {extra}'
        self.args += ' pipe:1'

class FFMpegAacEncoder(FFMpegEncoder):
    """Aac encoder.

    'bitrate' is expressed in kilobits.
    See also https://trac.ffmpeg.org/wiki/Encode/AAC.
    """

    container = 'adts'
    encoder = 'aac'

    def __init__(self):
        super().__init__(['audio/aac', 'audio/x-aac', 'audio/vnd.dlna.adts'])
        self.bitrate = 192

    def extra_args(self):
        return f'-b:a {self.bitrate}k'

class FFMpegAiffEncoder(FFMpegEncoder):
    """Lossless Aiff Encoder."""

    container = 'aiff'

    def __init__(self):
        super().__init__(['audio/aiff'])

class FFMpegFlacEncoder(FFMpegEncoder):
    """Lossless Flac encoder.

    See also https://ffmpeg.org/ffmpeg-all.html#flac-2.
    """

    container = 'flac'

    def __init__(self):
        super().__init__(['audio/flac', 'audio/x-flac'])

class FFMpegL16WavEncoder(L16Mixin, FFMpegEncoder):
    """Lossless PCM L16 encoder with a wav container."""

    container = 'wav'

    def __init__(self):
        FFMpegEncoder.__init__(self, ['audio/l16'], sample_format='s16be')

class FFMpegMp3Encoder(FFMpegEncoder):
    """Mp3 encoder.

    Setting 'bitrate' to 0 causes VBR encoding to be chosen and 'qscale'
    to be used instead, otherwise 'bitrate' is expressed in kilobits.
    See also https://trac.ffmpeg.org/wiki/Encode/MP3.
    """

    container = 'mp3'
    encoder = 'libmp3lame'

    def __init__(self):
        super().__init__(['audio/mp3', 'audio/mpeg'])
        self.bitrate = 256
        self.qscale = 2

    def extra_args(self):
        if self.bitrate != 0:
            return f'-b:a {self.bitrate}k'
        else:
            return f'-qscale:a {self.qscale}'

class FFMpegOpusEncoder(FFMpegEncoder):
    """Opus encoder.

    See also https://wiki.xiph.org/Opus_Recommended_Settings.
    """

    container = 'opus'
    encoder = 'libopus'

    def __init__(self):
        super().__init__(['audio/opus', 'audio/x-opus'])
        self.bitrate = 128

    def extra_args(self):
        return f'-b:a {self.bitrate}k'

class FFMpegVorbisEncoder(FFMpegEncoder):
    """Vorbis encoder.

    Setting 'bitrate' to 0 causes VBR encoding to be chosen and 'qscale'
    to be used instead, otherwise 'bitrate' is expressed in kilobits.
    See also https://ffmpeg.org/ffmpeg-all.html#libvorbis.
    """

    container = 'ogg'
    encoder = 'libvorbis'

    def __init__(self):
        super().__init__(['audio/vorbis', 'audio/x-vorbis'])
        self.bitrate = 256
        self.qscale = 3.0

    def extra_args(self):
        if self.bitrate != 0:
            return f'-b:a {self.bitrate}k'
        else:
            return f'-qscale:a {self.qscale}'
