%define pkgname CharisSIL

Summary:	Unicode serif font family for typography
Name:		fonts-ttf-charis-sil
Version:	4.110
Release:	2
License:	OFL
Group:		System/Fonts/True type
URL:		https://scripts.sil.org/cms/scripts/page.php?site_id=nrsi&item_id=CharisSILfont
Source0:	%{pkgname}-%{version}.zip
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch:	noarch
BuildRequires:	freetype-tools
BuildRequires:	dos2unix

%description
Charis is similar to Bitstream Charter, one of the first fonts designed
specifically for laser printers. It is highly readable and holds up well
in less-than-ideal reproduction environments. It also has a full set of styles
- regular, italic, bold, bold italic - and so is more useful in general
publishing than Doulos SIL. Charis is a serif, proportionally-spaced font
optimized for readability in long printed documents.

The goal for this product was to provide a single Unicode-based font family
that would contain a comprehensive inventory of glyphs needed for almost any
Roman- or Cyrillic-based writing system, whether used for phonetic
or orthographic needs. In addition, there is provision for other characters
and symbols useful to linguists. This font makes use of state-of-the-art font
technologies to support complex typographic issues, such as the need
to position arbitrary combinations of base glyphs and diacritics optimally. 


%prep
%setup -q -n %{pkgname}-%{version}
dos2unix *.txt

%build

%install
%__rm -rf %{buildroot}

%__mkdir_p %{buildroot}%{_xfontdir}/TTF/charis-sil

%__install -m 644 *.ttf %{buildroot}%{_xfontdir}/TTF/charis-sil
ttmkfdir %{buildroot}%{_xfontdir}/TTF/charis-sil -o %{buildroot}%{_xfontdir}/TTF/charis-sil/fonts.dir
%__ln_s fonts.dir %{buildroot}%{_xfontdir}/TTF/charis-sil/fonts.scale

%__mkdir_p %{buildroot}%_sysconfdir/X11/fontpath.d/
%__ln_s ../../..%{_xfontdir}/TTF/charis-sil \
    %{buildroot}%_sysconfdir/X11/fontpath.d/ttf-charis-sil:pri=50

%clean
%__rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc FONTLOG.txt OFL.txt OFL-FAQ.txt README.txt
%dir %{_xfontdir}/TTF/charis-sil
%{_xfontdir}/TTF/charis-sil/*.ttf
%verify(not mtime) %{_datadir}/fonts/TTF/charis-sil/fonts.dir
%{_xfontdir}/TTF/charis-sil/fonts.scale
%{_sysconfdir}/X11/fontpath.d/ttf-charis-sil:pri=50


%changelog
* Fri Dec 09 2011 Dmitry Mikhirev <dmikhirev@mandriva.org> 4.110-1mdv2012.0
+ Revision: 739471
- Update to 4.110

* Fri Jul 22 2011 Sergey Zhemoitel <serg@mandriva.org> 4.106-1
+ Revision: 690962
- imported package fonts-ttf-charis-sil

