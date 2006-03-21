Summary:	Xara Extreme LX Vector Image Editor
Summary(pl):	Edytor obraz�w wektorowych Xara Extreme LX
Name:		XaraLX
Version:	0.3r693
Release:	0.1
License:	GPL
Group:		X11/Applications
Source0:	http://downloads.xara.com/opensource/%{name}_%{version}.tar.bz2
# Source0-md5:	70c9490007e2d9914840f937ff28434d
URL:		http://www.xaraxtreme.org/
BuildRequires:	autoconf
BuildRequires:	automake
# ???
BuildRequires:	gettext-devel
BuildRequires:	libtool
BuildRequires:	perl-base
BuildRequires:	wxGTK2-unicode-devel >= 2.6.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Xara eXtreme is a 2D vector graphics editor created by a small British
software company named Xara, notable for being the first vector
graphics software product to provide fully anti-aliased display,
advanced gradient fill and transparency tools, now available in many
of the competitors' products. Xara X is also notable for its usability
and very fast renderer

%description -l pl
Xara eXtreme jest edytorem grafiki 2D stworzonym przez ma�� brytyjsk�
firm� Xara, pierwszym wektorowym programem udost�pniaj�cym pe�ny
anty-aliasing, rozbudowane wype�nianie gradientami i narz�dzia do
prze�roczysto�ci, teraz dost�pne w wielu innych produktach. Xara X
jest tak�e znana z u�yteczno�ci i pr�dko�ci dzia�ania.

%prep
%setup -q

%build
%{__gettextize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--with-wx-config=wx-gtk2-unicode-config
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
