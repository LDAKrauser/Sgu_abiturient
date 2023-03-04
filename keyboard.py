from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

kb_start = ReplyKeyboardMarkup(resize_keyboard=True,
                              one_time_keyboard=True)
b1_help = KeyboardButton('/help')
b2_desciption = KeyboardButton('/description')
b3_open_door = KeyboardButton('/open_door')
kb_start.add(b1_help).add(b2_desciption).add(b3_open_door)

ikb_faculty = InlineKeyboardMarkup(row_width=3)
ib1_biologi = InlineKeyboardButton(text='Биологически факультет',
                                   callback_data='od_biologi')
ib2_geographi = InlineKeyboardButton(text='Географический факультет',
                                     callback_data='od_geographi')
ib3_geology = InlineKeyboardButton(text='Геологический факультет',
                                   callback_data='od_geology')
ib4_csit = InlineKeyboardButton(text='Факультет компьютерных наук и информационных технологий',
                                callback_data='od_csit')
ib5_iimo = InlineKeyboardButton(text='Институт истории и международных отношений',
                                callback_data='od_iimo')
ib6_mathmech = InlineKeyboardButton(text='Механико-математический факультет',
                                    callback_data='od_mathmech')
ib7_phisic = InlineKeyboardButton(text='Институт физики',
                                  callback_data='od_phisic')
ib8_chemistry = InlineKeyboardButton(text='Институт химии',
                                     callback_data='od_chemistry')
ib9_economi = InlineKeyboardButton(text='Экономический факультет',
                                   callback_data='od_economi')
ib10_philosophy = InlineKeyboardButton(text='Философский факультет',
                                       callback_data='od_philosophy')
ib11_psychology = InlineKeyboardButton(text='Факультет психологии',
                                       callback_data='od_psychology')
ib12_sociology = InlineKeyboardButton(text='Социологический факультет',
                                      callback_data='od_sociology')
ib13_law = InlineKeyboardButton(text='Юридический факультет',
                                callback_data='od_law')
ib14_medic = InlineKeyboardButton(text='Факультет фундаментальной медицины и медицинских технологий',
                                  callback_data='od_medic')
ib15_pedagogical = InlineKeyboardButton(text='Факультет психолого-педагогического и специального образования',
                                        callback_data='od_pedagogical')
ib16_languages = InlineKeyboardButton(text='Факультет иностранных языков и лингводидактики',
                                      callback_data='od_languages')
ib17_arts = InlineKeyboardButton(text='Институт искусств',
                                 callback_data='od_arts')
ib18_sports = InlineKeyboardButton(text='Инстиут физической культуры и спорта',
                                   callback_data='od_sports')
ib19_journalistm = InlineKeyboardButton(text='Институт филологии и журналистики',
                                        callback_data='od_journalistm')
ib20_continuing = InlineKeyboardButton(text='Институт дополнительного профессионального образования',
                                       callback_data='od_continuing')
ib21_geologycolleg = InlineKeyboardButton(text='Геологический колледж',
                                          callback_data='od_geologycolleg')
ib22_radioelectronics = InlineKeyboardButton(text='Колледж радиоэлектроники',
                                             callback_data='od_radioelectronics')
ikb_faculty.add(ib1_biologi).add(ib2_geographi).add(ib3_geology).add(ib4_csit).add(ib5_iimo).add(ib6_mathmech).add(
    ib7_phisic).add(ib8_chemistry).add(ib9_economi).add(ib10_philosophy).add(ib11_psychology).add(ib12_sociology).add(
    ib13_law).add(ib14_medic).add(ib15_pedagogical).add(ib16_languages).add(ib17_arts).add(ib18_sports).add(
    ib19_journalistm).add(ib20_continuing).add(ib21_geologycolleg).add(ib22_radioelectronics)



#b20_continuing = KeyboardButton('/Institute_of_Continuing_Professional_Education')
#b21_geologycollega = KeyboardButton('/Geology_College')
#b22_radioelectronics = KeyboardButton('/College_of_Radioelectronics')
#kb_faculty.add(b1_biologi).insert(b2_geographi).add(b3_geology).insert(b4_csit).add(b5_iimo).insert(b6_mathmech).add(
#    b6_mathmech).insert(b7_physic).add(b8_chemistry).insert(b9_economi).add(b10_philosophy).insert(b11_psychology).add(
#    b12_sociology).insert(b13_law).add(b14_medic).insert(b15_pedagogical).add(b16_languages).insert(b17_arts).add(
#    b18_sports).insert(b19_journalistm).add(b20_continuing).insert(b21_geologycollega).add(b22_radioelectronics)