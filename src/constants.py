from types import SimpleNamespace

from src.utils.keyboard import create_keyboard
import emoji

keys = SimpleNamespace(
    settings=emoji.emojize(':gear: Settings'),
    exit=emoji.emojize(':cross_mark: Exit'),
    back=emoji.emojize(':arrow_left: Back')
)

keyboards = SimpleNamespace(
    main=create_keyboard(keys.settings),
)

states=SimpleNamespace(
    main='MAIN'
)
