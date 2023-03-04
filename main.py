from aiogram import Bot, Dispatcher, executor, types
from config import TOKEN_API
from keyboard import kb_start, ikb_faculty

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)

HELP_COMMAND = """
/help - список команд негры
/description - описание бота
/open_door - Дни открытых дверей 2023
"""


async def on_startup(_):
    print('Бот запущен!')


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await bot.send_sticker(message.from_user.id,
                           sticker="CAACAgIAAxkBAAEHCMNjrBD0d2t1OFxmdamUWBOyp3wcUwACIAADwZxgDGWWbaHi0krRLAQ")
    await message.answer('<em>Привет абитуриент! Чтобы посмотреть,что я умею,введи команду /help</em>',
                         parse_mode="HTML",
                         reply_markup=kb_start)
    await message.delete()


@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    await message.reply(text=HELP_COMMAND)


@dp.message_handler(commands=['description'])
async def disc_command(message: types.Message):
    await bot.send_message(message.from_user.id,
                           text=f'Привет {message.from_user.first_name}! Этот бот предназначет для упрощения процесса поступления в СГУ'
                                'им. Н.Г Чернышевского. Тут ты можешь найти основную информацию необходимую для подачи документов или задать вопрос'
                                'на который мы постараемся оперативно ответить.')
    await message.delete()


@dp.message_handler(commands=['open_door'])
async def op_door(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text='<em>Чтобы получить подробную информацию о Дне открытых дверей, выберите структурное подразделение</em>',
                           parse_mode="HTML",
                           reply_markup=ikb_faculty)
    await message.delete()


@dp.callback_query_handler(text='od_biologi')
async def od_biologi_call(callback: types.CallbackQuery):
    await bot.send_photo(callback.from_user.id,
                         photo="https://www.sgu.ru/sites/default/files/styles/220x---/public/dep-main-logo/biofak.png?itok=TCTUAsX8")
    await callback.message.answer(f'<b><i>Биологический факультет</i></b>\n'
                                  f'<a href="https://www.sgu.ru/structure/biological">Страница факультета</a>\n'
                                  f'<b><i>Дни открытых дверей в 2023 году:</i></b>\n'
                                  f'22.01.2023 (воскресенье) в 12:00;\n'
                                  f'23.04.2023 (воскресенье) в 12:00\n'
                                  f'По адресу: г.Саратов, ул. Астраханская, 83, 5 корпус, аудитория 61',
                                  parse_mode="HTML")
    await bot.send_location(chat_id=callback.from_user.id,
                            latitude=51.53800,
                            longitude=46.00984)
    await callback.answer()


@dp.callback_query_handler(text='od_geographi')
async def od_geographi_call(callback: types.CallbackQuery):
    await bot.send_photo(callback.from_user.id,
                         photo="https://www.sgu.ru/sites/default/files/styles/220x---/public/dep-main-logo/geograficheskiy.png?itok=1fFWlh6L")
    await callback.message.answer(f'<b><i>Географический факультет</i></b>\n'
                                  f'<a href="https://www.sgu.ru/structure/geographic">Страница факультета</a>\n'
                                  f'<b><i>Дни открытых дверей в 2023 году:</i></b>\n'
                                  f'19.02.2023 (воскресенье) в 11:00;\n'
                                  f'19.03.2023 (воскресенье) в 11:00\n'
                                  f'По адресу: г.Саратов, ул. Университетская, 59, 4 корпус, аудитория 16',
                                  parse_mode="HTML")
    await bot.send_location(chat_id=callback.from_user.id,
                            latitude=51.54068,
                            longitude=46.00594)
    await callback.answer()


@dp.callback_query_handler(text='od_geology')
async def od_geology_call(callback: types.CallbackQuery):
    await bot.send_photo(callback.from_user.id,
                         photo="https://www.sgu.ru/sites/default/files/styles/220x---/public/dep-main-logo/logo.png?itok=eVanzek4")
    await callback.message.answer(f'<b><i>Геологический факультет</i></b>\n'
                                  f'<a href="https://www.sgu.ru/structure/geological">Страница факультета</a>\n'
                                  f'<b><i>Дни открытых дверей в 2023 году:</i></b>\n'
                                  f'18.03.2023 (суббота) в 12:00\n'
                                  f'По адресу: г.Саратов, ул. Московская, 161, 6 корпус, Региональный музей Землеведения, аудитория 119',
                                  parse_mode="HTML")
    await bot.send_location(chat_id=callback.from_user.id,
                            latitude=51.54080,
                            longitude=46.00259)
    await callback.answer()


@dp.callback_query_handler(text='od_csit')
async def od_csit_call(callback: types.CallbackQuery):
    await bot.send_photo(callback.from_user.id,
                         photo="https://www.sgu.ru/sites/default/files/styles/220x---/public/dep-main-logo/kniit.png?itok=IqlRcn0F")
    await callback.message.answer(f'<b><i>Факультет компьютерных наук и информационных технологий</i></b>\n'
                                  f'<a href="https://www.sgu.ru/structure/computersciences">Страница факультета</a>\n'
                                  f'<b><i>Дни открытых дверей в 2023 году:</i></b>\n'
                                  f'15.01.2023 (воскресенье) в 11:00;\n'
                                  f'09.04.2023 (воскресенье) в 11:00;\n'
                                  f'24.06.2023 (воскресенье) в 11:00;\n'
                                  f'15.07.2023 (воскресенье) в 11:00\n'
                                  f'По адресу: г.Саратов, ул. Вольская, 10а (угол Белоглинской), 12 корпус, Актовый зал',
                                  parse_mode="HTML")
    await bot.send_location(chat_id=callback.from_user.id,
                            latitude=51.52313,
                            longitude=46.01999)
    await callback.answer()


@dp.callback_query_handler(text='od_iimo')
async def od_iimo_call(callback: types.CallbackQuery):
    await bot.send_photo(callback.from_user.id,
                         photo="https://www.sgu.ru/sites/default/files/styles/220x---/public/dep-main-logo/emblema.png?itok=kWyPtZFh")
    await callback.message.answer(f'<b><i>Институт истории и международных отношений</i></b>\n'
                                  f'<a href="https://www.sgu.ru/structure/imimo">Страница института</a>\n'
                                  f'<b><i>Дни открытых дверей в 2023 году:</i></b>\n'
                                  f'23.04.2023 (воскресенье) в 12:00\n'
                                  f'По адресу: г.Саратов, ул. Астраханская, 83, 11 корпус, аудитория 408',
                                  parse_mode="HTML")
    await bot.send_location(chat_id=callback.from_user.id,
                            latitude=51.53842,
                            longitude=46.00929)
    await callback.answer()


@dp.callback_query_handler(text='od_mathmech')
async def od_mathmech_call(callback: types.CallbackQuery):
    await bot.send_photo(callback.from_user.id,
                         photo="https://www.sgu.ru/sites/default/files/styles/220x---/public/dep-main-logo/logo_1.png?itok=9M-4PGMe")
    await callback.message.answer(f'<b><i>Механико-математически факультет</i></b>\n'
                                  f'<a href="https://www.sgu.ru/structure/mechmath">Страница факультета</a>\n'
                                  f'<b><i>Дни открытых дверей в 2023 году:</i></b>\n'
                                  f'21.01.2023 (суббота) в 14:00\n'
                                  f'<b><i>Ночь открытых дверей в 2023 году:</i></b>\n'
                                  f'19.05.2023 (пятница) в 18:00\n'
                                  f'По адресу: г.Саратов, ул. Б. Казачья, 112, 9 корпус, аудитория 401',
                                  parse_mode="HTML")
    await bot.send_location(chat_id=callback.from_user.id,
                            latitude=51.53792,
                            longitude=46.00856)
    await callback.answer()


@dp.callback_query_handler(text='od_phisic')
async def od_phisic_call(callback: types.CallbackQuery):
    await bot.send_photo(callback.from_user.id,
                         photo="https://www.sgu.ru/sites/default/files/styles/500x375_4x3/public/dep-main-pic/2022-10/img_0745_3.jpg?itok=8Lpn3yCy")
    await callback.message.answer(f'<b><i>Институт физики</i></b>\n'
                                  f'<a href="https://www.sgu.ru/structure/physicsinstitute">Страница института</a>\n'
                                  f'<b><i>Дни открытых дверей в 2023 году:</i></b>\n'
                                  f'19.02.2023 (воскресенье) в 12:00\n'
                                  f'По адресу: г.Саратов, ул. Университетская, 40, 3 корпус, Большая физическая аудитория',
                                  parse_mode="HTML")
    await bot.send_location(chat_id=callback.from_user.id,
                            latitude=51.53891,
                            longitude=46.00571)
    await callback.answer()


@dp.callback_query_handler(text='od_chemistry')
async def od_chemistry_call(callback: types.CallbackQuery):
    await bot.send_photo(callback.from_user.id,
                         photo="https://www.sgu.ru/sites/default/files/styles/220x---/public/dep-main-logo/inchem_logo220.png?itok=XkUyCyVB")
    await callback.message.answer(f'<b><i>Институт химии</i></b>\n'
                                  f'<a href="https://www.sgu.ru/structure/chemical">Страница института</a>\n'
                                  f'<b><i>Дни открытых дверей в 2023 году:</i></b>\n'
                                  f'19.03.2023 (воскресенье) в 11:00\n'
                                  f'По адресу: г.Саратов, ул. Московская, 155, 1 корпус, Нижняя аудитория',
                                  parse_mode="HTML")
    await bot.send_location(chat_id=callback.from_user.id,
                            latitude=51.53912,
                            longitude=46.00915)
    await callback.answer()


@dp.callback_query_handler(text='od_economi')
async def od_economi_call(callback: types.CallbackQuery):
    await bot.send_photo(callback.from_user.id,
                         photo="https://www.sgu.ru/sites/default/files/styles/220x---/public/dep-main-logo/ekonomicheskiy_fakultet_0.png?itok=y0G34XDz")
    await callback.message.answer(f'<b><i>Экономический факультет</i></b>\n'
                                  f'<a href="https://www.sgu.ru/structure/economy">Страница факультета</a>\n'
                                  f'<b><i>Дни открытых дверей в 2023 году:</i></b>\n'
                                  f'21.01.2023 (суббота) в 15:00;\n'
                                  f'22.04.2023 (суббота) в 15:00\n'
                                  f'По адресу: г.Саратов, ул. Вольская, 10а (угол Белоглинской), 12 корпус, аудитория 433',
                                  parse_mode="HTML")
    await bot.send_location(chat_id=callback.from_user.id,
                            latitude=51.52313,
                            longitude=46.01999)
    await callback.answer()


@dp.callback_query_handler(text='od_philosophy')
async def od_philosophy_call(callback: types.CallbackQuery):
    await bot.send_photo(callback.from_user.id,
                         photo="https://www.sgu.ru/sites/default/files/styles/220x---/public/dep-main-logo/logotip_ff_4.png?itok=pFVBGEsc")
    await callback.message.answer(f'<b><i>Философский факультет</i></b>\n'
                                  f'<a href="https://www.sgu.ru/structure/philosophic">Страница факультета</a>\n'
                                  f'<b><i>Дни открытых дверей в 2023 году:</i></b>\n'
                                  f'27.01.2023 (пятница) в 15:00;\n'
                                  f'17.02.2023 (суббота) в 15:00;\n'
                                  f'21.04.2023 (суббота) в 15:00;\n'
                                  f'По адресу: г.Саратов, ул. Вольская, 10а (угол Белоглинской), 12 корпус, аудитория 203',
                                  parse_mode="HTML")
    await bot.send_location(chat_id=callback.from_user.id,
                            latitude=51.52313,
                            longitude=46.01999)
    await callback.answer()


@dp.callback_query_handler(text='od_psychology')
async def od_psychology_call(callback: types.CallbackQuery):
    await bot.send_photo(callback.from_user.id,
                         photo='https://www.sgu.ru/sites/default/files/pictures/2020/04/21/lyudi-iriski_0.jpeg')
    await callback.message.answer(f"<b><i>Факультет психологии</i></b>\n"
                                  f"<a href=\"https://www.sgu.ru/structure/fps\">Страница факультета</a>\n"
                                  f"<b><i>Дни открытых дверей в 2023 году:</i></b>\n"
                                  f"19.02.2023 (воскресенье) в 12:00;\n"
                                  f"09.04.2023 (воскресенье) в 12:00\n"
                                  f"По адресу: г.Саратов, ул. Вольская, 10а (угол Белоглинской), 12 корпус, Актовый зал",
                                  parse_mode="HTML")
    await bot.send_location(chat_id=callback.from_user.id,
                            latitude=51.52313,
                            longitude=46.01999)
    await callback.answer()


@dp.callback_query_handler(text='od_sociology')
async def od_sociology_call(callback: types.CallbackQuery):
    await bot.send_photo(callback.from_user.id,
                         photo="https://www.sgu.ru/sites/default/files/styles/220x---/public/dep-main-logo/logo_standart.png?itok=Mt4PDrJx")
    await callback.message.answer(f'<b><i>Социологический факультет</i></b>\n'
                                  f'<a href="https://www.sgu.ru/structure/sociological">Страница факультета</a>\n'
                                  f'<b><i>Дни открытых дверей в 2023 году:</i></b>\n'
                                  f'12.02.2023 (воскресенье) в 11:00;\n'
                                  f'19.03.2023 (воскресенье) в 11:00\n'
                                  f'По адресу: г.Саратов, ул. Б. Казачья, 120, 7 корпус, аудитория 216',
                                  parse_mode="HTML")
    await bot.send_location(chat_id=callback.from_user.id,
                            latitude=51.53949,
                            longitude=46.00161)
    await callback.answer()


@dp.callback_query_handler(text='od_law')
async def od_law_call(callback: types.CallbackQuery):
    await bot.send_photo(callback.from_user.id,
                         photo="https://www.sgu.ru/sites/default/files/styles/220x---/public/dep-main-logo/yuridicheskiy_fakultet.png?itok=9_2GfPdP")
    await callback.message.answer(f'<b><i>Юридический факультет</i></b>\n'
                                  f'<a href="https://www.sgu.ru/structure/jurist">Страница факультета</a>\n'
                                  f'<b><i>Дни открытых дверей в 2023 году:</i></b>\n'
                                  f'29.01.2023 (воскресенье) в 12:00;\n'
                                  f'21.04.2023 (пятница) в 16:00\n'
                                  f'По адресу: г.Саратов, ул. Вольская, 10а (угол Белоглинской), 12 корпус, Актовый зал',
                                  parse_mode="HTML")
    await bot.send_location(chat_id=callback.from_user.id,
                            latitude=51.52313,
                            longitude=46.01999)
    await callback.answer()


@dp.callback_query_handler(text='od_medic')
async def od_medic_call(callback: types.CallbackQuery):
    await bot.send_photo(callback.from_user.id,
                         photo="https://www.sgu.ru/sites/default/files/styles/220x---/public/dep-main-logo/logo_3.png?itok=5MDnJszh")
    await callback.message.answer(f'<b><i>Факультет фундаментальной медицины и медицинских технологий</i></b>\n'
                                  f'<a href="https://www.sgu.ru/structure/ffmimt">Страница факультета</a>\n'
                                  f'<b><i>Дни открытых дверей в 2023 году:</i></b>\n'
                                  f'15.04.2023 (суббота) в 12:00;\n'
                                  f'21.06.2023 (среда) в 12:00\n'
                                  f'По адресу: г.Саратов, ул. Б. Казачья, 112а, 8 корпус, аудитория 420',
                                  parse_mode="HTML")
    await bot.send_location(chat_id=callback.from_user.id,
                            latitude=51.53831,
                            longitude=46.00668)
    await callback.answer()


@dp.callback_query_handler(text='od_pedagogical')
async def od_pedagogical_call(callback: types.CallbackQuery):
    await bot.send_photo(callback.from_user.id,
                         photo="https://www.sgu.ru/sites/default/files/styles/220x---/public/dep-main-logo/emblema_fakulteta_-_kopiya_0.png?itok=YrVD4_Xf")
    await callback.message.answer(f'<b><i>Факультет психолого-педагогического и специального образования</i></b>\n'
                                  f'<a href="https://www.sgu.ru/structure/fppiso">Страница факультета</a>\n'
                                  f'<b><i>Дни открытых дверей в 2023 году:</i></b>\n'
                                  f'28.01.2023 (суббота) в 11:00;\n'
                                  f'19.03.2023 (воскресенье) в 11:00;\n'
                                  f'16.04.2023 (воскресенье) в 11:00\n'
                                  f'По адресу: г.Саратов, ул. Вольская, 10а (угол Белоглинской), 12 корпус, аудитория 328',
                                  parse_mode="HTML")
    await bot.send_location(chat_id=callback.from_user.id,
                            latitude=51.52313,
                            longitude=46.01999)
    await callback.answer()


@dp.callback_query_handler(text='od_languages')
async def od_lenguages_call(callback: types.CallbackQuery):
    await bot.send_photo(callback.from_user.id,
                         photo="https://www.sgu.ru/sites/default/files/styles/220x---/public/dep-main-logo"
                               "/fakultet_inostrannyh_yazykov.png?itok=8yr_Vt03")
    await callback.message.answer(f'<b><i>Факультет иностранных языков и лингводидактики</i></b>\n'
                                  f'<a href="https://www.sgu.ru/structure/fi">Страница факультета</a>\n'
                                  f'<b><i>Дни открытых дверей в 2023 году:</i></b>\n'
                                  f'12.02.2023 (воскресенье) в 12:00;\n'
                                  f'23.04.2023 (воскресенье) в 12:00\n'
                                  f'По адресу: г.Саратов, ул. Заулошнова, 3, 16 корпус, аудитория 302',
                                  parse_mode="HTML")
    await bot.send_location(chat_id=callback.from_user.id,
                            latitude=51.52297,
                            longitude=46.02101)
    await callback.answer()


@dp.callback_query_handler(text='od_arts')
async def od_arts_call(callback: types.CallbackQuery):
    await bot.send_photo(callback.from_user.id,
                         photo="https://www.sgu.ru/sites/default/files/styles/220x---/public/dep-main-logo"
                               "/logo_dlya_dokumentov_cvet.png?itok=QSynNDlC")
    await callback.message.answer(f'<b><i>Институт искусств</i></b>\n'
                                  f'<a href="https://www.sgu.ru/structure/instisk">Страница института</a>\n'
                                  f'<b><i>Дни открытых дверей в 2023 году:</i></b>\n'
                                  f'22.01.2023 (воскресенье) в 10:00;\n'
                                  f'19.03.2023 (воскресенье) в 10:00\n'
                                  f'По адресу: г.Саратов, ул. Заулошнова, 5, 17 корпус, аудитория 21',
                                  parse_mode="HTML")
    await bot.send_location(chat_id=callback.from_user.id,
                            latitude=51.52343,
                            longitude=46.02131)
    await callback.answer()


@dp.callback_query_handler(text='od_sports')
async def od_sports_call(callback: types.CallbackQuery):
    await bot.send_photo(callback.from_user.id,
                         photo="https://www.sgu.ru/sites/default/files/styles/220x---/public/dep-main-logo/ifkis.png"
                               "?itok=-kFlvkJx")
    await callback.message.answer(f'<b><i>Институт физической культуры и спорта</i></b>\n'
                                  f'<a href="https://www.sgu.ru/structure/ifkis">Страница института</a>\n'
                                  f'<b><i>Дни открытых дверей в 2023 году:</i></b>\n'
                                  f'18.02.2023 (суббота) в 11:00;\n'
                                  f'15.04.2023 (суббота) в 11:00\n'
                                  f'По адресу: г.Саратов, ул. Вольская, 10 (угол Белоглинской), 15 корпус, аудитория 8',
                                  parse_mode="HTML")
    await bot.send_location(chat_id=callback.from_user.id,
                            latitude=51.52370,
                            longitude=46.01978)
    await callback.answer()


@dp.callback_query_handler(text='od_journalistm')
async def od_journalistm_call(callback: types.CallbackQuery):
    await bot.send_photo(callback.from_user.id,
                         photo="https://www.sgu.ru/sites/default/files/styles/220x---/public/dep-main-logo/logo_0.png"
                               "?itok=lVSdUJcb")
    await callback.message.answer(f'<b><i>Институт филологии и журналистики</i></b>\n'
                                  f'<a href="https://www.sgu.ru/structure/philological">Страница института</a>\n'
                                  f'<b><i>Дни открытых дверей в 2023 году:</i></b>\n'
                                  f'28.01.2023 (суббота) в 15:00;\n'
                                  f'22.04.2023 (суббота) в 15:00\n'
                                  f'По адресу: г.Саратов, ул. Астраханская, 83, 11 корпус, аудитория 208',
                                  parse_mode="HTML")
    await bot.send_location(chat_id=callback.from_user.id,
                            latitude=51.53842,
                            longitude=46.00929)
    await callback.answer()


@dp.callback_query_handler(text='od_continuing')
async def od_continuing_call(callback: types.CallbackQuery):
    await bot.send_photo(callback.from_user.id,
                         photo="https://www.sgu.ru/sites/default/files/styles/500x375_4x3/public/dep-main-pic/2022-08"
                               "/otkrytye_dveri_pp.jpg?itok=Y4ZuCq9w")
    await callback.message.answer(f'<b><i>Институт дополнительного профессионального образования</i></b>\n'
                                  f'<a href="https://www.sgu.ru/idpo">Страница института</a>\n'
                                  f'<b><i>Дни открытых дверей в 2023 году:</i></b>\n'
                                  f'18.01.2023 (среда) в 15:30;\n'
                                  f'15.02.2023 (среда) в 15:30;\n'
                                  f'22.03.2023 (среда) в 15:30;\n'
                                  f'19.04.2023 (среда) в 15:30;\n'
                                  f'24.05.2023 (среда) в 15:30;\n'
                                  f'14.06.2023 (среда) в 15:00\n'
                                  f'По адресу: г.Саратов, ул. Вольская, 10а (угол Белоглинской), 12 корпус, аудитория 614',
                                  parse_mode="HTML")
    await bot.send_location(chat_id=callback.from_user.id,
                            latitude=51.52313,
                            longitude=46.01999)
    await callback.answer()


@dp.callback_query_handler(text='od_geologycolleg')
async def od_geologycolleg_call(callback: types.CallbackQuery):
    await bot.send_photo(callback.from_user.id,
                         photo="https://www.sgu.ru/sites/default/files/styles/220x---/public/dep-main-logo/sgu.png"
                               "?itok=m1Az5F7H")
    await callback.message.answer(f'<b><i>Геологический колледж</i></b>\n'
                                  f'<a href="https://www.sgu.ru/structure/geolkol">Страница колледжа</a>\n'
                                  f'<b><i>Дни открытых дверей в 2023 году:</i></b>\n'
                                  f'14.01.2023 (суббота) в 14:00;\n'
                                  f'11.02.2023 (суббота) в 14:00;\n'
                                  f'11.03.2023 (суббота) в 14:00;\n'
                                  f'18.04.2023 (суббота) в 14:00;\n'
                                  f'13.05.2023 (суббота) в 14:00\n'
                                  f'По адресу: г.Саратов, ул. Ак. Антонова, 10, аудитория 120',
                                  parse_mode="HTML")
    await bot.send_location(chat_id=callback.from_user.id,
                            latitude=51.60159,
                            longitude=45.98188)
    await callback.answer()


@dp.callback_query_handler(text='od_radioelectronics')
async def od_radioelectronics_call(callback: types.CallbackQuery):
    await bot.send_photo(callback.from_user.id,
                         photo="https://www.sgu.ru/sites/default/files/styles/220x---/public/dep-main-logo/new2.png"
                               "?itok=4YmlkwNB")
    await callback.message.answer(f'<b><i>Колледж радиоэлектроники</i></b>\n'
                                  f'<a href="https://www.sgu.ru/structure/yablkol">Страница колледжа</a>\n'
                                  f'<b><i>Дни открытых дверей в 2023 году:</i></b>\n'
                                  f'21.01.2023 (суббота) в 16:00;\n'
                                  f'18.02.2023 (суббота) в 16:00;\n'
                                  f'18.03.2023 (суббота) в 16:00;\n'
                                  f'22.04.2023 (суббота) в 16:00;\n'
                                  f'20.05.2023 (суббота) в 16:00\n'
                                  f'По адресу: г.Саратов, ул. Астраханская, 77, Большой актовый зал или Малый актовый зал',
                                  parse_mode="HTML")
    await bot.send_location(chat_id=callback.from_user.id,
                            latitude=51.53586,
                            longitude=46.00854)
    await callback.answer()


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup, skip_updates=True)
