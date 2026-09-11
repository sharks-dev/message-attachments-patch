# message-attachments-patch

This patch adds a paperclip button to the conversation page in the Jolla-messages app.

The paperclip opens a filepicker where you can select an image to send to the recipient.

Clicking the image will send it and any text that was previously in the text field.

### NOTE:

<mark>This patch does not work flawlessly out-of-the-box</mark>, as the sailjail permissions of jolla-messages must be modified to allow it to access your gallery.

`sailjaild` does not notice patchmanager's overlays on its own. You need to `devel-su touch /usr/share/applications/jolla-messages.desktop` so that it reloads the updated file. This must be done each time you enable the patch (ie. each reboot).

#### Screenshots:

<table>
  <td><img src="https://raw.githubusercontent.com/sharks-dev/message-attachments-patch/refs/heads/main/screenshots/1-compose.png" alt="Compose a message" width="200"/></td>
  <td><img src="https://raw.githubusercontent.com/sharks-dev/message-attachments-patch/refs/heads/main/screenshots/2-picker.png" alt="Select an image" width="200"/></td>
  <td><img src="https://raw.githubusercontent.com/sharks-dev/message-attachments-patch/refs/heads/main/screenshots/3-sent.png" alt="Sent!" width="200"/></td>
</table>
