pkgname = "umbriel"
pkgver = "0_git20261026"
pkgrel = 0

_gitver = "76477c2"
build_style = "meson"
configure_args = ["--prefix=/usr", "--buildtype=release", "-Dtests=enabled"]
hostmakedepends = ["meson", "pkgconf", "wayland-progs", "bash"]
makedepends = [
    "cairo-devel",
    "elogind-devel",
    "wlroots0.20-devel",
    "libxkbcommon-devel",
    "lcms2-devel",
    "libdisplay-info",
    "libdrm-devel",
    "libei-devel",
    "libinput-devel",
    "libxcb-devel",
    "mesa-devel",
    "mesa-gbm-devel",
    "mesa-gles2-libs",
    "nlohmann-json",
    "pixman-devel",
    "pango-devel",
    "tomlplusplus-devel",
    "udev-devel",
    "wayland-devel",
    "wayland-protocols",
    "xcb-util-wm-devel",
]
checkdepends = ["xcb-util-renderutil-devel"]
pkgdesc = "Wayland compositor built on wlroots"
license = "MIT"
url = "https://noctalia.dev"
source = f"https://github.com/noctalia-dev/umbriel/archive/{_gitver}.tar.gz"
sha256 = "1eb9ec4ba7a123c7a45a760fd836eb253e7bba49dbe6d2b468b7fc2c7826290e"

options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
    self.uninstall("usr/lib/systemd/user")
