Name:       message-attachments-patch

BuildArch: noarch

Summary:    Message Attachments
Version:    0.0.1
Release:    1
Group:      Qt/Qt
License:    WTFPL
Source0:    %{name}-%{version}.tar.bz2
Requires:   patchmanager
Requires:   jolla-messages

%description
Add attachments button to messages app so that you can select pictures from the conversation screen.

%prep
%setup -q -n %{name}-%{version}

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/patchmanager/patches/message_attachments
cp -r patch/* %{buildroot}/usr/share/patchmanager/patches/message_attachments

%pre
if [ -d /var/lib/patchmanager/ausmt/patches/message_attachments ]; then
/usr/sbin/patchmanager -u message_attachments || true
fi

%preun
if [ -d /var/lib/patchmanager/ausmt/patches/message_attachments ]; then
/usr/sbin/patchmanager -u message_attachments || true
fi

%files
%defattr(-,root,root,-)
%{_datadir}/patchmanager/patches/message_attachments 
