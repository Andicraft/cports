pkgname = "umbriel"
pkgver = "0_git20261107"
pkgrel = 0
_gitver = "f5dd36b"
build_style = "meson"
configure_args = ["--prefix=/usr", "--buildtype=release", "-Dtests=enabled"]
hostmakedepends = ["meson", "pkgconf", "wayland-progs", "bash"]
makedepends = [
    "cairo-devel",
    "elogind-devel",
    "lcms2-devel",
    "libdisplay-info",
    "libdrm-devel",
    "libei-devel",
    "libinput-devel",
    "libxcb-devel",
    "libxkbcommon-devel",
    "mesa-devel",
    "mesa-gbm-devel",
    "mesa-gles2-libs",
    "nlohmann-json",
    "pango-devel",
    "pixman-devel",
    "tomlplusplus-devel",
    "udev-devel",
    "wayland-devel",
    "wayland-protocols",
    "wlroots0.20-devel",
    "xcb-util-wm-devel",
]
checkdepends = ["xcb-util-renderutil-devel"]
pkgdesc = "Wayland compositor built on wlroots"
license = "MIT"
url = "https://noctalia.dev"
source = f"https://github.com/noctalia-dev/umbriel/archive/{_gitver}.tar.gz"
sha256 = "92b92c15f97e1de7e359c8f35aedcfaab549551d36a17b318844b8fb552e5170"

options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
    self.uninstall("usr/lib/systemd/user")
