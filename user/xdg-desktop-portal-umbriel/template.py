pkgname = "xdg-desktop-portal-umbriel"
pkgver = "0_git20261024"
pkgrel = 0
_gitver = "e69d6f7"
build_style = "meson"
configure_args = ["--prefix=/usr", "--buildtype=release"]
hostmakedepends = ["meson", "pkgconf", "wayland-progs", "git"]
makedepends = [
    "cairo-devel",
    "gtk4-devel",
    "libdrm-devel",
    "mesa-gbm-devel",
    "nlohmann-json",
    "pipewire-devel",
    "sdbus-cpp-devel",
    "tomlplusplus-devel",
    "wayland-devel",
    "wayland-protocols",
]
checkdepends = ["xcb-util-renderutil-devel"]
pkgdesc = "Umbriel's xdg-desktop-portal"
license = "MIT"
url = "https://noctalia.dev"
source = f"https://github.com/noctalia-dev/xdg-desktop-portal-umbriel/archive/{_gitver}.tar.gz"
sha256 = "1f1e82afdedfa9d766506c1b35657256a93dfd29635d5f0580d58df773347d46"

options = []


def post_install(self):
    self.install_license("LICENSE")
    self.uninstall("usr/lib/systemd/user")
