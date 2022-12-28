%global oname youtube-dl-gui

# This package use a fork of the original project at
#   https://github.com/MrS0m30n3/youtube-dl-gui
# because the author won't port the code to python3.
# It is a different package because it uses a
# different versioning schema with respect to the
# original code.

Summary:	Front-end GUI of the popular youtube-dl
Name:		yt-dlg
Version:	1.8.4
Release:	2
License:	Public Domain
Group:		Video
Url:		https://github.com/oleksis/%{oname}/
Source0:	https://github.com/oleksis/%{oname}/archive/refs/tags/v%{version}/%{oname}-%{version}.tar.gz
BuildRequires:	python3dist(polib)
BuildRequires:	python3dist(pypubsub)
BuildRequires:	python3dist(pip)
BuildRequires:	python3dist(setuptools)
BuildRequires:	python3dist(wheel)
BuildRequires:	python3dist(wxpython)
#BuildRequires:	ffmpeg

Requires:	python3
Requires:	python3dist(wxpython)
Recommends:	ffmpeg

BuildArch:	noarch

%rename		youtube-dl-gui
Conflicts:	youtube-dl-pyqt

%description
A cross platform front-end GUI of the popular youtube-dl written in wxPython.

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{python3_sitelib}/youtube_dl_gui/
%{python3_sitelib}/yt_dlg-*.*-info/
%{_datadir}/applications/*.desktop
%{_datadir}/pixmaps/%{oname}.png
%{_iconsdir}/hicolor/*/apps/%{oname}.png
%{_mandir}/man1/%{name}.1*

#-----------------------------------------------------------------------------

%prep
%autosetup -p1 -n %{oname}-%{version}

# fix unmet dependencies
sed -i -e "/pyinstaller<=/d" -e "/wxPython<=/d" setup.py

%build
%py_build

%install
%py_install

# fix manpage name
mv %{buildroot}%{_mandir}/man1/%{oname}.1 %{buildroot}%{_mandir}/man1/%{name}.1

# .desktop
# from upstream commit commit effd7b72bf1cc4d37ab98dd745fe573a1eb1c292
install -pm 0755 -d %{buildroot}%{_datadir}/applications/
cat > %{buildroot}%{_datadir}/applications/%{name}.desktop << EOF
[Desktop Entry]
Name=Youtube Downloader GUI
GenericName=Youtube Downloader GUI
Comment=A cross platform front-end GUI of the popular youtube-dl written in wxPython Phoenix
Exec=yt-dlg
Icon=youtube-dl-gui
MimeType=
Terminal=False
Type=Application
Categories=AudioVideo;Utility;
Keywords=Multimedia;Video;Audio;
EOF
#desktop-file-install \
#	--remove-category="X-GNOME-NetworkSettings" \
#	--dir %{buildroot}%{_datadir}/applications  \
#	%{name}.desktop

# locales
#find_lang %{name} --with-qt

