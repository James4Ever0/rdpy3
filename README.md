# rdpy3- for Python3 

**this is a fork for porting rdpy3to Python3**

Remote Desktop Protocol in twisted python.

rdpy3is a pure Python implementation of the Microsoft RDP (Remote Desktop Protocol) protocol (client and server side). rdpy3is built over the event driven network engine Twisted. rdpy3support standard RDP security layer, RDP over SSL and NLA authentication (through ntlmv2 authentication protocol).

rdpy3provides the following RDP and VNC binaries:
* RDP Man In The Middle proxy which record session
* RDP Honeypot
* RDP screenshoter
* RDP client
* VNC client
* VNC screenshoter
* RSS Player

## Build

rdpy3is fully implemented in python, except the bitmap decompression algorithm which is implemented in C for performance purposes.

### Dependencies

Dependencies are only needed for pyqt5 binaries :
* rdpy3-rdpclient
* rdpy3-rdpscreenshot
* rdpy3-vncclient
* rdpy3-vncscreenshot
* rdpy3-rssplayer

#### Linux

Example for Debian based systems :
```
sudo apt-get install python3-pyqt5
```

#### OS X
Example for OS X to install PyQt with homebrew
```
$ brew install qt sip pyqt
```

#### Windows

install PyQt5 and PyWin32

## rdpy3Binaries

rdpy3comes with some very useful binaries. These binaries are linux and windows compatible.

### rdpy3-rdpclient

rdpy3-rdpclient is a simple RDP Qt5 client.

```
$ rdpy3-rdpclient.py [-u username] [-p password] [-d domain] [-r rss_ouput_file] [...] XXX.XXX.XXX.XXX[:3389]
```

You can use rdpy3-rdpclient in a Recorder Session Scenario, used in rdpy3-rdphoneypot.

### rdpy3-vncclient

rdpy3-vncclient is a simple VNC Qt5 client .

```
$ rdpy3-vncclient.py [-p password] XXX.XXX.XXX.XXX[:5900]
```

### rdpy3-rdpscreenshot

rdpy3-rdpscreenshot saves login screen in file.

```
$ rdpy3-rdpscreenshot.py [-w width] [-l height] [-o output_file_path] XXX.XXX.XXX.XXX[:3389]
```

### rdpy3-vncscreenshot

rdpy3-vncscreenshot saves the first screen update in file.

```
$ rdpy3-vncscreenshot.py [-p password] [-o output_file_path] XXX.XXX.XXX.XXX[:5900]
```

### rdpy3-rdpmitm

rdpy3-rdpmitm is a RDP proxy allows you to do a Man In The Middle attack on RDP protocol.
Record Session Scenario into rss file which can be replayed by rdpy3-rssplayer.

```
$ rdpy3-rdpmitm.py -o output_dir [-l listen_port] [-k private_key_file_path] [-c certificate_file_path] [-r (for XP or server 2003 client)] target_host[:target_port]
```

Output directory is used to save the rss file with following format (YYYYMMDDHHMMSS_ip_index.rss)
The private key file and the certificate file are classic cryptographic files for SSL connections. The RDP protocol can negotiate its own security layer If one of both parameters are omitted, the server use standard RDP as security layer.

### rdpy3-rdphoneypot

rdpy3-rdphoneypot is an RDP honey Pot. Use Recorded Session Scenario to replay scenario through RDP Protocol.

```
$ rdpy3-rdphoneypot.py [-l listen_port] [-k private_key_file_path] [-c certificate_file_path] rss_file_path_1 ... rss_file_path_N
```

The private key file and the certificate file are classic cryptographic files for SSL connections. The RDP protocol can negotiate its own security layer. If one of both parameters are omitted, the server use standard RDP as security layer.
You can specify more than one files to match more common screen size.

### rdpy3-rssplayer

rdpy3-rssplayer is use to replay Record Session Scenario (rss) files generates by either rdpy3-rdpmitm or rdpy3-rdpclient binaries.

```
$ rdpy3-rssplayer.py rss_file_path
```

## rdpy3Qt Widget

rdpy3can also be used as Qt widget through rdpy3.ui.qt5.QRemoteDesktop class. It can be embedded in your own Qt application. qt5reactor must be used in your app for Twisted and Qt to work together. For more details, see sources of rdpy3-rdpclient.

## rdpy3library

In a nutshell rdpy3can be used as a protocol library with a twisted engine.

### Simple RDP Client

```python
from rdpy3.protocol.rdp import rdp

class MyRDPFactory(rdp.ClientFactory):

    def clientConnectionLost(self, connector, reason):
        reactor.stop()

    def clientConnectionFailed(self, connector, reason):
        reactor.stop()

    def buildObserver(self, controller, addr):

        class MyObserver(rdp.RDPClientObserver):

            def onReady(self):
                """
                @summary: Call when stack is ready
                """
                #send 'r' key
                self._controller.sendKeyEventUnicode(ord(unicode("r".toUtf8(), encoding="UTF-8")), True)
                #mouse move and click at pixel 200x200
                self._controller.sendPointerEvent(200, 200, 1, true)

            def onUpdate(self, destLeft, destTop, destRight, destBottom, width, height, bitsPerPixel, isCompress, data):
                """
                @summary: Notify bitmap update
                @param destLeft: xmin position
                @param destTop: ymin position
                @param destRight: xmax position because RDP can send bitmap with padding
                @param destBottom: ymax position because RDP can send bitmap with padding
                @param width: width of bitmap
                @param height: height of bitmap
                @param bitsPerPixel: number of bit per pixel
                @param isCompress: use RLE compression
                @param data: bitmap data
                """
                
            def onSessionReady(self):
		        """
		        @summary: Windows session is ready
		        """

            def onClose(self):
                """
                @summary: Call when stack is close
                """

        return MyObserver(controller)

from twisted.internet import reactor
reactor.connectTCP("XXX.XXX.XXX.XXX", 3389, MyRDPFactory())
reactor.run()
```

### Simple RDP Server
```python
from rdpy3.protocol.rdp import rdp

class MyRDPFactory(rdp.ServerFactory):

    def buildObserver(self, controller, addr):

        class MyObserver(rdp.RDPServerObserver):

            def onReady(self):
                """
                @summary: Call when server is ready
                to send and receive messages
                """

            def onKeyEventScancode(self, code, isPressed):
                """
                @summary: Event call when a keyboard event is catch in scan code format
                @param code: scan code of key
                @param isPressed: True if key is down
                @see: rdp.RDPServerObserver.onKeyEventScancode
                """

            def onKeyEventUnicode(self, code, isPressed):
                """
                @summary: Event call when a keyboard event is catch in unicode format
                @param code: unicode of key
                @param isPressed: True if key is down
                @see: rdp.RDPServerObserver.onKeyEventUnicode
                """

            def onPointerEvent(self, x, y, button, isPressed):
                """
                @summary: Event call on mouse event
                @param x: x position
                @param y: y position
                @param button: 1, 2, 3, 4 or 5 button
                @param isPressed: True if mouse button is pressed
                @see: rdp.RDPServerObserver.onPointerEvent
                """

            def onClose(self):
                """
                @summary: Call when human client close connection
                @see: rdp.RDPServerObserver.onClose
                """

        return MyObserver(controller)

from twisted.internet import reactor
reactor.listenTCP(3389, MyRDPFactory())
reactor.run()
```

### Simple VNC Client
```python
from rdpy3.protocol.rfb import rfb

class MyRFBFactory(rfb.ClientFactory):

    def clientConnectionLost(self, connector, reason):
        reactor.stop()

    def clientConnectionFailed(self, connector, reason):
        reactor.stop()

    def buildObserver(self, controller, addr):
        class MyObserver(rfb.RFBClientObserver):

            def onReady(self):
                """
                @summary: Event when network stack is ready to receive or send event
                """

            def onUpdate(self, width, height, x, y, pixelFormat, encoding, data):
                """
                @summary: Implement RFBClientObserver interface
                @param width: width of new image
                @param height: height of new image
                @param x: x position of new image
                @param y: y position of new image
                @param pixelFormat: pixefFormat structure in rfb.message.PixelFormat
                @param encoding: encoding type rfb.message.Encoding
                @param data: image data in accordance with pixel format and encoding
                """

            def onCutText(self, text):
                """
                @summary: event when server send cut text event
                @param text: text received
                """

            def onBell(self):
                """
                @summary: event when server send biiip
                """

            def onClose(self):
                """
                @summary: Call when stack is close
                """

        return MyObserver(controller)

from twisted.internet import reactor
reactor.connectTCP("XXX.XXX.XXX.XXX", 3389, MyRFBFactory())
reactor.run()
```
