def askOnExit():
  if askokcancel("Подтверждение",
     "Вы действительно хотите выйти из программы?"):
    app.destroy()

app = TApplication("Первая форма")
app.position = (100, 300)
app.size = (500, 200)
app.resizable = (True, False)
app.minsize = (100, 200)
app.onCloseQuery = askOnExit

app.run()



