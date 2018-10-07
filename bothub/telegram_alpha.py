import requests

base_url = "https://api.telegram.org/bot{token}/{method}"

def api_token(context):
    for ch in context['channel']['channels']:
        if ch['type'] == 'telegram':
            return ch['api_key']

def send_chat_action(event, context, action):
    """Tell the user that something is happening on the bot's side.

    Args:
        action (String): typing | upload_photo | record_video | upload_video | record_audio | upload_audio |
                         upload_document | find_location | record_video_note | upload_video_note
    """
    token = api_token(context)
    if token is None:
        raise ValueError('No token in the context dict')

    url = base_url.format(token=token, method='sendChatAction')

    headers = {'Content-Type': 'application/json'}

    payload = {
        'chat_id': event['chat_id'],
        'action': action
    }

    r = requests.post(url, json=payload, headers=headers)

    if r.status_code == requests.codes.ok:
        return r.json().get('ok')
    else:
        return False

def send_photo(event, context, photo):
    """Send a photo.

    Args:
        photo (String): Image URL
    """
    token = api_token(context)
    if token is None:
        raise ValueError('No token in the context dict')

    url = base_url.format(token=token, method='sendPhoto')

    headers = {'Content-Type': 'application/json'}

    payload = {
        'chat_id': event['chat_id'],
        'photo': photo
    }

    r = requests.post(url, json=payload, headers=headers)

    if r.status_code == requests.codes.ok:
        return r.json().get('ok')
    else:
        return False

