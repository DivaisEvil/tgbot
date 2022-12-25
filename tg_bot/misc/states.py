from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from tg_bot.misc.test import Test

async  def test_q(message):
    #text = 'вы начали тестировать '
    await  message.answer(#'Вы начали тестирование\n'
                          #'Вопрос  №1\n'
                          #'Вам нравиться писать код?'
                          ' Ваше имя'
    )
    await Test.Q1.set()
async  def ansewer_q1(message: types.Message, state: FSMContext):
    text = 'вы начали тестировать '
    answer = message.text
    await state.update_data(answer=answer)
    await message.answer(#" Вопрос  №2\n"
                         #"Вам нравиться учиться? "
                         "Ваш Email")
    await Test.Q2.set()

async  def ansewer_q2(message: types.Message, state: FSMContext):
    text = 'вы начали тестировать '
    answer = message.text
    await state.update_data(answer3=answer)
    await message.answer(#" Вопрос  №3\n"
                         #"Вам нравиться учиться?"
                         "Ваш Телефон")
    await Test.Q3.set()

async  def ansewer_q3(message: types.Message, state: FSMContext):
    # answer = message.text
    # await state.update_data(answer=answer)
    # await message.answer(" Вопрос  №1\n"
    #                      "Вам нравиться учиться?")
    data = await state.get_data()
    answer1 = data.get('answer')
    answer2 = data.get('answer3')
    answer3 = message.text

    await  message.answer(f"Привет! Ты ввел следующие данные:\nИмя - {answer1}\nEmail - {answer2}\nТелефон - {answer3}")
    #await message.answer(f"ответ 1: {answer1}")
    #await message.answer(f"ответ 2: {answer2}")
    #await message.answer(f"ответ 3: {answer3}")
    await state.reset_state(with_data=False)

def register_test_q(dp: Dispatcher):
    print("тест")
    dp.register_message_handler(test_q, state="*", regexp="/form")
    dp.register_message_handler(ansewer_q1, state= Test.Q1)
    dp.register_message_handler(ansewer_q2, state=Test.Q2)
    dp.register_message_handler(ansewer_q3, state=Test.Q3)
