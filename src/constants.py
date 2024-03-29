from types import SimpleNamespace

from src.utils.keyboard import create_keyboard
import emoji

keys = SimpleNamespace(
    settings=emoji.emojize(':gear: Settings'),
    back=emoji.emojize(':arrow_left: Back'),
    next=emoji.emojize(':arrow_right: Next'),
    add=emoji.emojize(':heavy_plus_sign: Add'),
    edit=emoji.emojize(':pencil: Edit'),
    save=emoji.emojize(':heavy_check_mark: Save')
    cancel=emoji.emojize(':x: Cancel'),
    delete=emoji.emojize('wastebasket: Delete'),
    yes=emoji.emojize(':white_check_mark: Yes'),
    no=emoji.emojize(':negative_squared_cross_mark: No'), 
    ask_question=emoji.emojize(':question: Ask a question),

)

keyboards = SimpleNamespace(
    main=create_keyboard(keys.settings),
)

states=SimpleNamespace(
    main='MAIN',
    ask_question='ASK_QUESTION'
)
