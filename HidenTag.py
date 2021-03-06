from .. import loader, utils


def register(cb):
    cb(HidenTagMod())

class HidenTagMod(loader.Module):
    """Скрытый тегнуть пользователя."""
    strings = {'name': 'HidenTag'}

    async def tagcmd(self, message):
        """Использование: .tag <@> <текст (по желанию)>."""
        args = utils.get_args_raw(message).split(' ')
        tag = ' '
        try:
            user = await message.client.get_entity(args[0])
        except:
            return await message.edit('Пользователь удалён из контактов.')
        await message.delete()
        if len(args) == 1:
            tag = tag
        elif len(args) >= 2:
            tag = utils.get_args_raw(message).split(' ', 1)[1]
        await message.client.send_message(message.to_id, f'{tag} <a href="tg://user?id={user.id}">\u2060</a>')
