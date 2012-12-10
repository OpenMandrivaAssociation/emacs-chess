%define pname chess
%define name emacs-%pname

Name:		%name
Summary: 	A client and library for playing Chess from Emacs.
Version: 	2.0b5
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
%setup -q -n %pname-%version

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

%changelog
* Sat Aug 05 2006 Olivier Thauvin <nanardon@mandriva.org>
+ 08/05/06 15:50:35 (53315)
- rebuild

* Sat Aug 05 2006 Olivier Thauvin <nanardon@mandriva.org>
+ 08/05/06 15:48:58 (53314)
Import emacs-chess

* Mon May 01 2006 Olivier Thauvin <nanardon@mandriva.org> 2.0b5-3mdk
- Rebuild

* Fri Apr 29 2005 Thierry Vignaud <tvignaud@mandrakesoft.com> 2.0b5-2mdk
- rebuild for latest emacs

* Wed Apr 21 2004 Olivier Thauvin <thauvin@aerov.jussieu.fr> 2.0b5-1mdk
- 2.0b5

* Tue Dec 23 2003 Michael Scherer <misc@mandrake.org> 2.0b3-3mdk
- BuildRequires : texinfo
 

* Tue Jan 21 2003 Thierry Vignaud <tvignaud@mandrakesoft.com> 2.0b3-2mdk
- rebuild for latest emacs

* Sun Dec 29 2002 Olivier Thauvin <thauvin@aerov.jussieu.fr> 2.0b3-1mdk
- initial mdk package

