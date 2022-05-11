Name:           recycle_bin
Version:        1.0.0
Release:        1.el7
Summary:        recycle bin for linux

BuildArch:      noarch

License:        GPLv3
Source0:        rm
Source1:        recyclebin

Requires:       at

%description
recycle bin for linux

%prep

%build

%install
rm -rf $RPM_BUILD_ROOT
install -dm 755 $RPM_BUILD_ROOT/usr/local/bin/
install -dm 755 $RPM_BUILD_ROOT/opt/RecycleBin_installed/
install -pm 755  %{SOURCE0} $RPM_BUILD_ROOT/opt/RecycleBin_installed/
install -pm 755  %{SOURCE1} $RPM_BUILD_ROOT/usr/local/bin/

%clean

%files
%defattr(755,root,root,-)
/opt/RecycleBin_installed/rm
%defattr(755,root,root,-)
/usr/local/bin/recyclebin

%changelog
* Tue May 10 2022 Charalampos Madenidis <charrismadenidis@gmail.com> - 1.0.0
- First version of recycle bin
