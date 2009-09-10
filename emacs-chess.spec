%define pname chess
%define name emacs-%pname

Name:		%name
Summary: 	A client and library for playing Chess from Emacs
Version: 	2.0b6
Release: 	%mkrel 4
License:	GPL
Group: 		Editors
Source: 	%{pname}-%{version}.tar.bz2
Url: 		http://www.newartisans.com/johnw/EmacsChess.html
BuildRequires: 	emacs-bin
BuildRequires:  texinfo
BuildArch: noarch
BuildRoot: 	%{_tmppath}/%{name}-%{version}-root

%{expand:%%define emacs_version %(rpm -q emacs|sed 's/emacs-\([0-9].*\)-.*$/\1/')}

%description
Chess.el does not know how to play chess against you.  While the
library does know all legal moves, there is no "thinking" module.  For
this, you must download one of the publically available chess engines,
such as gnuchess, crafty or phalanx.  You will find all of these
sufficiently challenging, I'm sure.  Once they are installed, chess.el
will use them, provided the locations of the binaries is on your PATH.

%prep 
%setup -q -n %pname

%build
make clean
%make

%install
rm -fr $RPM_BUILD_ROOT/*
mkdir -p $RPM_BUILD_ROOT/%_datadir/emacs/site-lisp
install	*.el *.elc $RPM_BUILD_ROOT/%_datadir/emacs/site-lisp

install -d %buildroot%{_sysconfdir}/emacs/site-start.d
cp chess-auto.el %buildroot%{_sysconfdir}/emacs/site-start.d/%pname-emacs.el

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc COPYING ChangeLog EPD.txt PGN.txt PLAN README TODO 
%_datadir/emacs/site-lisp/*.el
%_datadir/emacs/site-lisp/*.elc
%config(noreplace) %_sysconfdir/emacs/site-start.d/%pname-emacs.el
