from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import Toplevel
from tkinter import messagebox
from datetime import datetime, timedelta
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++ТАБЛИЦА ПРИЛЕТОВ++++++++++++++++++++++++++++++++++++++++++++++++
def show_flight_table():
    # Создаем новое окно
    global tag
    flight_window = Toplevel(W_main)
    flight_window.title("Влеты в аэропорт Кольцово")
    flight_window.geometry("1200x750")
    flight_window.resizable(False, False)

    # Загружаем изображение баннера
    banner_image = PhotoImage(file="banner_up.png")

    # Создаем виджет Label для баннера
    banner_label = Label(flight_window, image=banner_image, borderwidth=0)
    banner_label.image = banner_image  # Сохраняем ссылку на изображение
    banner_label.pack(side=TOP, fill=X)

    # Загружаем изображение фона
    background_image = Image.open("bg for reisi.png")
    background_photo = ImageTk.PhotoImage(background_image)

    # Создаем Canvas для отображения фона
    canvas = Canvas(flight_window, width=1200, height=666, borderwidth=0)
    canvas.pack(fill=BOTH, expand=True)

    # Добавляем изображение фона на Canvas
    canvas.create_image(0, 0, image=background_photo, anchor=NW)

    # Размеры таблицы
    frame = Frame(canvas, bg='white')
    frame.place(x=115, y=143, width=969, height=433)

    # Создаем виджет Treeview для таблицы
    tree = ttk.Treeview(frame, columns=("time", "destination", "flight", "status"), show='headings')

    # Определяем заголовки колонок
    tree.heading("time", text="ВРЕМЯ", command=lambda: sort_column(tree, "time", False))
    tree.heading("destination", text="НАПРАВЛЕНИЕ", command=lambda: sort_column(tree, "destination", False))
    tree.heading("flight", text="РЕЙС", command=lambda: sort_column(tree, "flight", False))
    tree.heading("status", text="СТАТУС", command=lambda: sort_column(tree, "status", False))

    # Определяем ширину колонок
    tree.column("time", width=100, anchor=CENTER)
    tree.column("destination", width=300, anchor=CENTER)
    tree.column("flight", width=185, anchor=CENTER)
    tree.column("status", width=184, anchor=CENTER)

    # Пример данных для таблицы
    flights = [
        ("13:15", "Казань", "T1234", "Вылетел"),
        ("14:00", "Сочи", "A5678", "Ожидается"),
        ("15:30", "Владивосток", "B9101", "Задержан"),
        ("16:45", "Краснодар", "C1123", "Отменен"),
        ("17:00", "Самара", "D4567", "Вылетел"),
        ("18:30", "Уфа", "E8910", "Ожидается"),
        ("19:15", "Пермь", "F1112", "Задержан"),
        ("20:00", "Ростов-на-Дону", "G1314", "Отменен"),
        ("21:30", "Челябинск", "H1516", "Вылетел"),
        ("22:45", "Воронеж", "I1718", "Ожидается"),
        ("23:00", "Иркутск", "J1920", "Задержан"),
        ("00:30", "Тюмень", "K2122", "Отменен"),
        ("01:15", "Омск", "L2324", "Вылетел"),
        ("02:00", "Барнаул", "M2526", "Ожидается"),
        ("03:30", "Сургут", "N2728", "Задержан"),
        ("04:45", "Хабаровск", "O2930", "Отменен"),
        ("05:00", "Нижний Новгород", "P3132", "Вылетел"),
        ("06:30", "Калининград", "Q3334", "Ожидается"),
        ("07:15", "Мурманск", "R3536", "Задержан"),
        ("08:00", "Архангельск", "S3738", "Отменен"),
        ("09:30", "Ставрополь", "T3940", "Вылетел"),
        ("10:45", "Волгоград", "U4142", "Ожидается"),
        ("11:00", "Кемерово", "V4344", "Задержан"),
        ("12:30", "Томск", "W4546", "Отменен"),
        ("13:15", "Киров", "X4748", "Вылетел"),
        ("14:00", "Астрахань", "Y4950", "Ожидается"),
        ("15:30", "Белгород", "Z5152", "Задержан"),
        ("16:45", "Чебоксары", "A5354", "Отменен"),
        ("17:00", "Курган", "B5556", "Вылетел"),
        ("18:30", "Магнитогорск", "C5758", "Ожидается"),
        ("19:15", "Симферополь", "D5960", "Задержан"),
        ("06:30", "Калининград", "Q3334", "Ожидается"),
        ("07:15", "Мурманск", "R3536", "Задержан"),
        ("08:00", "Архангельск", "S3738", "Отменен"),
        ("09:30", "Ставрополь", "T3940", "Вылетел"),
        ("10:45", "Волгоград", "U4142", "Ожидается"),
        ("11:00", "Кемерово", "V4344", "Задержан"),
        ("12:30", "Томск", "W4546", "Отменен"),
        ("13:15", "Киров", "X4748", "Вылетел"),
        ("14:00", "Астрахань", "Y4950", "Ожидается"),
        ("15:30", "Белгород", "Z5152", "Задержан"),
        ("16:45", "Чебоксары", "A5354", "Отменен"),
        ("17:00", "Курган", "B5556", "Вылетел"),
        ("18:30", "Магнитогорск", "C5758", "Ожидается"),
        ("19:15", "Симферополь", "D5960", "Задержан")
    ]

    # Добавляем данные в таблицу с тегами
    for flight in flights:
        status = flight[3]
        if status == "Вылетел":
            tag = 'departed'
        elif status == "Задержан":
            tag = 'delayed'
        elif status == "Отменен":
            tag = 'cancelled'
        tree.insert("", END, values=flight, tags=(tag))

    # Упаковываем таблицу
    tree.pack(expand=YES, fill=BOTH)

    # Настраиваем шрифты для таблицы
    style = ttk.Style()
    style.configure("Treeview.Heading", font=("Montserrat", 20, "bold"), foreground="dark blue")
    style.configure("Treeview", font=("Montserrat", 13, "normal"), background="dark blue")

    # Применяем стиль к строкам
    tree.tag_configure('departed', background='white')
    tree.tag_configure('delayed', background='white')
    tree.tag_configure('cancelled', background='white')

    flight_window.grab_set()
    flight_window.mainloop()

    def sort_column(tree, col, reverse):
        l = [(tree.set(k, col), k) for k in tree.get_children('')]
        l.sort(reverse=reverse)

        for index, (val, k) in enumerate(l):
            tree.move(k, '', index)

        tree.heading(col, command=lambda: sort_column(tree, col, not reverse))

    def sort_column(tree, col, reverse):
        l = [(tree.set(k, col), k) for k in tree.get_children('')]
        l.sort(reverse=reverse)

        for index, (val, k) in enumerate(l):
            tree.move(k, '', index)

        tree.heading(col, command=lambda: sort_column(tree, col, not reverse))

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++ТАБЛИЦА ВЛЕТОВ++++++++++++++++++++++++++++++++++++++++++++++++++
def show_offflight_table():
    # Создаем новое окно
    global tag
    flight_window = Toplevel(W_main)
    flight_window.title("Влеты в аэропорт Кольцово")
    flight_window.geometry("1200x750")
    flight_window.resizable(False, False)

    # Загружаем изображение баннера
    banner_image = PhotoImage(file="banner_up.png")

    # Создаем виджет Label для баннера
    banner_label = Label(flight_window, image=banner_image, borderwidth=0)
    banner_label.image = banner_image  # Сохраняем ссылку на изображение
    banner_label.pack(side=TOP, fill=X)

    # Загружаем изображение фона
    background_image = Image.open("bg for reisi1.png")
    background_photo = ImageTk.PhotoImage(background_image)

    # Создаем Canvas для отображения фона
    canvas = Canvas(flight_window, width=1200, height=666, borderwidth=0)
    canvas.pack(fill=BOTH, expand=True)

    # Добавляем изображение фона на Canvas
    canvas.create_image(0, 0, image=background_photo, anchor=NW)

    # Размеры таблицы
    frame = Frame(canvas, bg='white')
    frame.place(x=115, y=143, width=969, height=433)

    # Создаем виджет Treeview для таблицы
    tree = ttk.Treeview(frame, columns=("time", "destination", "flight", "status"), show='headings')

    # Определяем заголовки колонок
    tree.heading("time", text="ВРЕМЯ", command=lambda: sort_column(tree, "time", False))
    tree.heading("destination", text="НАПРАВЛЕНИЕ", command=lambda: sort_column(tree, "destination", False))
    tree.heading("flight", text="РЕЙС", command=lambda: sort_column(tree, "flight", False))
    tree.heading("status", text="СТАТУС", command=lambda: sort_column(tree, "status", False))

    # Определяем ширину колонок
    tree.column("time", width=100, anchor=CENTER)
    tree.column("destination", width=300, anchor=CENTER)
    tree.column("flight", width=185, anchor=CENTER)
    tree.column("status", width=184, anchor=CENTER)

    # Пример данных для таблицы
    flights = [
        ("13:15", "Казань", "T1234", "Вылетел"),
        ("14:00", "Сочи", "A5678", "Ожидается"),
        ("15:30", "Владивосток", "B9101", "Задержан"),
        ("16:45", "Краснодар", "C1123", "Отменен"),
        ("17:00", "Самара", "D4567", "Вылетел"),
        ("18:30", "Уфа", "E8910", "Ожидается"),
        ("19:15", "Пермь", "F1112", "Задержан"),
        ("20:00", "Ростов-на-Дону", "G1314", "Отменен"),
        ("21:30", "Челябинск", "H1516", "Вылетел"),
        ("22:45", "Воронеж", "I1718", "Ожидается"),
        ("23:00", "Иркутск", "J1920", "Задержан"),
        ("00:30", "Тюмень", "K2122", "Отменен"),
        ("01:15", "Омск", "L2324", "Вылетел"),
        ("02:00", "Барнаул", "M2526", "Ожидается"),
        ("03:30", "Сургут", "N2728", "Задержан"),
        ("04:45", "Хабаровск", "O2930", "Отменен"),
        ("05:00", "Нижний Новгород", "P3132", "Вылетел"),
        ("06:30", "Калининград", "Q3334", "Ожидается"),
        ("07:15", "Мурманск", "R3536", "Задержан"),
        ("08:00", "Архангельск", "S3738", "Отменен"),
        ("09:30", "Ставрополь", "T3940", "Вылетел"),
        ("10:45", "Волгоград", "U4142", "Ожидается"),
        ("11:00", "Кемерово", "V4344", "Задержан"),
        ("12:30", "Томск", "W4546", "Отменен"),
        ("13:15", "Киров", "X4748", "Вылетел"),
        ("14:00", "Астрахань", "Y4950", "Ожидается"),
        ("15:30", "Белгород", "Z5152", "Задержан"),
        ("16:45", "Чебоксары", "A5354", "Отменен"),
        ("17:00", "Курган", "B5556", "Вылетел"),
        ("18:30", "Магнитогорск", "C5758", "Ожидается"),
        ("19:15", "Симферополь", "D5960", "Задержан"),
        ("06:30", "Калининград", "Q3334", "Ожидается"),
        ("07:15", "Мурманск", "R3536", "Задержан"),
        ("08:00", "Архангельск", "S3738", "Отменен"),
        ("09:30", "Ставрополь", "T3940", "Вылетел"),
        ("10:45", "Волгоград", "U4142", "Ожидается"),
        ("11:00", "Кемерово", "V4344", "Задержан"),
        ("12:30", "Томск", "W4546", "Отменен"),
        ("13:15", "Киров", "X4748", "Вылетел"),
        ("14:00", "Астрахань", "Y4950", "Ожидается"),
        ("15:30", "Белгород", "Z5152", "Задержан"),
        ("16:45", "Чебоксары", "A5354", "Отменен"),
        ("17:00", "Курган", "B5556", "Вылетел"),
        ("18:30", "Магнитогорск", "C5758", "Ожидается"),
        ("19:15", "Симферополь", "D5960", "Задержан")
    ]

    # Добавляем данные в таблицу с тегами
    for flight in flights:
        status = flight[3]
        if status == "Вылетел":
            tag = 'departed'
        elif status == "Задержан":
            tag = 'delayed'
        elif status == "Отменен":
            tag = 'cancelled'
        tree.insert("", END, values=flight, tags=(tag))

    # Упаковываем таблицу
    tree.pack(expand=YES, fill=BOTH)

    # Настраиваем шрифты для таблицы
    style = ttk.Style()
    style.configure("Treeview.Heading", font=("Montserrat", 20, "bold"), foreground="dark blue")
    style.configure("Treeview", font=("Montserrat", 13, "normal"), background="dark blue")

    # Применяем стиль к строкам
    tree.tag_configure('departed', background='white')
    tree.tag_configure('delayed', background='white')
    tree.tag_configure('cancelled', background='white')

    flight_window.grab_set()
    flight_window.mainloop()

def sort_column(tree, col, reverse):
    l = [(tree.set(k, col), k) for k in tree.get_children('')]
    l.sort(reverse=reverse)

    for index, (val, k) in enumerate(l):
        tree.move(k, '', index)

    tree.heading(col, command=lambda: sort_column(tree, col, not reverse))

def sort_column(tree, col, reverse):
    l = [(tree.set(k, col), k) for k in tree.get_children('')]
    l.sort(reverse=reverse)

    for index, (val, k) in enumerate(l):
        tree.move(k, '', index)

    tree.heading(col, command=lambda: sort_column(tree, col, not reverse))


#+++++++++++++++++++++++++++++++++++++++++++++++++++++++СОЗДАНИЕ ОКНА++++++++++++++++++++++++++++++++++++++++++++++++
W_main = Tk()
W_main.config(width=1200, height=750)
W_main.resizable(False, False)
BackPhoto = PhotoImage(file="W_main.png")

L1 = Label(W_main, image=BackPhoto)
L1.place(x=-2, y=-1)

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++ЭТАЖИ АЭРОПОРТА++++++++++++++++++++++++++++++++++++++++++++++++
def floor1():
    W_flor1 = Toplevel(W_main)
    W_flor1.config(width=1200, height=750)
    W_flor1.resizable(False, False)
    BackPhoto = PhotoImage(file="flor 1.png")
    mapTEXT = PhotoImage(file="СХЕМА АЭРОПОРТА.png")

    mapPhoto1 = PhotoImage(file="Схема 1.png")
    mapPhoto2 = PhotoImage(file="Схема 2.png")
    mapPhoto3 = PhotoImage(file="Схема 3.png")

    B_floor1_choosed = PhotoImage(file="Этаж 1 выбран.png")
    B_floor2_choosed = PhotoImage(file="Этаж 2 выбран.png")
    B_floor3_choosed = PhotoImage(file="Этаж 3 выбран.png")

    B_floor1_naved = PhotoImage(file="Этаж 1 наведен.png")
    B_floor2_naved = PhotoImage(file="Этаж 2 наведен.png")
    B_floor3_naved = PhotoImage(file="Этаж 3 наведен.png")

    B_floor1_unchoosed = PhotoImage(file="Этаж 1 не выбран.png")
    B_floor2_unchoosed = PhotoImage(file="Этаж 2 не выбран.png")
    B_floor3_unchoosed = PhotoImage(file="Этаж 3 не выбран.png")

    L1 = Label(W_flor1, image=BackPhoto, borderwidth=0)
    L1.place(x=-1, y=-1)

    L2 = Label(W_flor1, image=mapTEXT, borderwidth=0)
    L2.place(x=422, y=120)

    L3 = Label(W_flor1, image=mapPhoto1, borderwidth=0)
    L3.place(x=60, y=159)

    def B_1_navod(e):
        if B_1floor["image"] == B_floor1_choosed:
            B_1floor["image"] = B_floor1_choosed

    def B_1_otvod(e):
        while B_1floor["image"] == B_floor1_choosed:
            B_1floor["image"] = B_floor1_choosed
            if B_1floor["image"] == B_floor1_naved:
                B_1floor["image"] = B_floor1_unchoosed

    def B_2_navod(e):
        if B_2floor["image"] == B_floor2_choosed:
            B_2floor["image"] = B_floor2_choosed

    def B_2_otvod(e):
        while B_2floor["image"] == B_floor2_choosed:
            B_2floor["image"] = B_floor2_choosed
            if B_2floor["image"] == B_floor2_naved:
                B_2floor["image"] = B_floor2_unchoosed

    def B_3_navod(e):
        if B_3floor["image"] == B_floor3_choosed:
            B_3floor["image"] = B_floor3_choosed

    def B_3_otvod(e):
        while B_3floor["image"] == B_floor3_choosed:
            B_3floor["image"] = B_floor3_choosed
            if B_3floor["image"] == B_floor3_naved:
                B_3floor["image"] = B_floor3_unchoosed

    def B_1_click():
        B_1floor["image"] = B_floor1_choosed
        B_2floor["image"] = B_floor2_unchoosed
        B_3floor["image"] = B_floor3_unchoosed
        L3["image"] = mapPhoto1

    def B_2_click():
        B_2floor["image"] = B_floor2_choosed
        B_1floor["image"] = B_floor1_unchoosed
        B_3floor["image"] = B_floor3_unchoosed
        L3["image"] = mapPhoto2

    def B_3_click():
        B_3floor["image"] = B_floor3_choosed
        B_2floor["image"] = B_floor2_unchoosed
        B_1floor["image"] = B_floor1_unchoosed
        L3["image"] = mapPhoto3

    B_1floor = Button(W_flor1, image=B_floor1_choosed,
                      borderwidth=0, command=B_1_click)
    B_1floor.place(x=1025, y=159, width=90, height=29)
    B_1floor.bind("<Enter>", B_1_navod)
    B_1floor.bind("<Leave>", B_1_otvod)

    B_2floor = Button(W_flor1, image=B_floor2_unchoosed,
                      borderwidth=0, command=B_2_click)
    B_2floor.place(x=1025, y=210, width=92, height=29)
    B_2floor.bind("<Enter>", B_2_navod)
    B_2floor.bind("<Leave>", B_2_otvod)

    B_3floor = Button(W_flor1, image=B_floor3_unchoosed,
                      borderwidth=0, command=B_3_click)
    B_3floor.place(x=1025, y=261, width=92, height=29)
    B_3floor.bind("<Enter>", B_3_navod)
    B_3floor.bind("<Leave>", B_3_otvod)

    W_flor1.grab_set()
    mainloop()
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++БИЛЕТЫ++++++++++++++++++++++++++++++++++++++++++++++++
def open_ticket_window():
    ticket_window = Toplevel(W_main)
    ticket_window.title("Ticket Booking")
    ticket_window.geometry("1200x750")
    ticket_window.resizable(False, False)

    selected_seats = []

    def toggle_seat(row, col):
        if (row, col) in selected_seats:
            selected_seats.remove((row, col))
            seat_buttons[row][col].config(image=chair)
        else:
            selected_seats.append((row, col))
            seat_buttons[row][col].config(image=chaired)

    def purchase_tickets():
        date = date_combobox.get()
        city = city_combobox.get()
        num_tickets = len(selected_seats)

        if not date or not city:
            messagebox.showwarning("Input Error", "Please select both date and city.")
            return

        if num_tickets == 0:
            messagebox.showwarning("Selection Error", "Please select at least one seat.")
            return

        # Calculate total cost based on city
        city_prices = {
            "New York": 100,
            "London": 150,
            "Paris": 120,
            "Tokyo": 200
        }
        total_cost = city_prices.get(city, 0) * num_tickets

        # Create a new window for the receipt
        receipt_window = Toplevel(ticket_window)
        receipt_window.title("Receipt")
        receipt_window.geometry("300x600")
        receipt_window.resizable(False, False)

        receipt_text = (f"Receipt for your purchase:\n"
                        f"\nDate: {date}\nCity: {city}\n"
                        f"\nSelected Seats:\n")
        for row, col in selected_seats:
            receipt_text += f"Row {row + 1}, Seat {col + 1}\n"
        receipt_text += f"\nTotal Cost: ${total_cost}"

        receipt_label = Label(receipt_window, text=receipt_text, justify=LEFT)
        receipt_label.pack(pady=20, padx=20)

        # Reset selections
        for row, col in selected_seats:
            seat_buttons[row][col].config(image=chair)
        selected_seats.clear()
        date_combobox.set('')
        city_combobox.set('')

    # Load background image
    bg_image = Image.open("T.png")
    bg_photo = ImageTk.PhotoImage(bg_image)

    chair = PhotoImage(file="chair.png")
    chaired = PhotoImage(file="chaired.png")

    buy_B = PhotoImage(file="buy_B.png")
    # Create a label to hold the background image
    bg_label = Label(ticket_window, image=bg_photo)
    bg_label.image = bg_photo  # Keep a reference to avoid garbage collection
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)

    # Create seat buttons
    seat_buttons = []
    for row in range(2):
        row_buttons = []
        for col in range(16):
            btn = Button(ticket_window, width=40, height=40, image=chair, borderwidth=0,
                         command=lambda r=row, c=col: toggle_seat(r, c))
            btn.place(x=210 + col * 45, y=330 + row * 45)  # Adjust position and size as needed
            row_buttons.append(btn)
        seat_buttons.append(row_buttons)

    # Create Combobox for date selection
    date_combobox = ttk.Combobox(ticket_window, values=[(datetime.now().date() + timedelta(days=i)).strftime("%Y-%m-%d") for i in range(30)])
    date_combobox.place(x=520, y=550, width=300, height=30)

    # Create Combobox for city selection
    city_combobox = ttk.Combobox(ticket_window, values=["New York", "London", "Paris", "Tokyo"])
    city_combobox.place(x=520, y=500, width=300, height=30)

    # Create purchase button
    purchase_button = Button(ticket_window, width=360, height=60, image=buy_B, borderwidth=0,
                             command=purchase_tickets).place(x=520, y=640)

    purchase_button.place(x=50, y=700)

    ticket_window.grab_set()
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++КНОПКИ++++++++++++++++++++++++++++++++++++++++++++++++
B_out_close = PhotoImage(file="out_close.png")
B_tickets_close = PhotoImage(file="ticket_close.png")
B_import_close = PhotoImage(file="import_close.png")
B_map_close = PhotoImage(file="map_close.png")
B_out_open = PhotoImage(file="out_open.png")
B_tickets_open = PhotoImage(file="tickets_open.png")
B_import_open = PhotoImage(file="import_open.png")
B_map_open = PhotoImage(file="map_open.png")

def navod_na_Bout(e):
    B_out['image'] = B_out_open
def navod_na_Bticket(e):
    B_ticket['image'] = B_tickets_open
def navod_na_Bimport(e):
    B_import['image'] = B_import_open
def navod_na_Bmap(e):
    B_map['image'] = B_map_open

def otvod_s_Bout(e):
    B_out['image'] = B_out_close
def otvod_s_Bticket(e):
    B_ticket['image'] = B_tickets_close
def otvod_s_Bimport(e):
    B_import['image'] = B_import_close
def otvod_s_Bmap(e):
    B_map['image'] = B_map_close


B_out = Button(W_main, image=B_out_close, borderwidth=0, command=show_flight_table)
B_out.place(x=125, y=139, width=250, height=447)
B_out.bind("<Enter>", navod_na_Bout)
B_out.bind("<Leave>", otvod_s_Bout)

B_ticket = Button(W_main, image=B_tickets_close, borderwidth=0, command=open_ticket_window)
B_ticket.place(x=475, y=139, width=250, height=420)
B_ticket.bind("<Enter>", navod_na_Bticket)
B_ticket.bind("<Leave>", otvod_s_Bticket)

B_import = Button(W_main, image=B_import_close, borderwidth=0, command=show_offflight_table)
B_import.place(x=825, y=139, width=250, height=447)
B_import.bind("<Enter>", navod_na_Bimport)
B_import.bind("<Leave>", otvod_s_Bimport)

B_map = Button(W_main, image=B_map_close, borderwidth=0, command = floor1)
B_map.place(x=380, y=632, width=439, height=61)
B_map.bind("<Enter>", navod_na_Bmap)
B_map.bind("<Leave>", otvod_s_Bmap)

W_main.mainloop()
