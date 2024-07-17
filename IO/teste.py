import tkinter as tk
from tkinter import *
from tkinter import ttk

# Create the main application window
root = tk.Tk()
root.geometry("1156x834")
root.config(background="#080121")


root.title("Diario")



image_frame = Canvas(root, width=660, height=400,background="#080121")
image_frame.place(x=742, y=360)
logo_img = PhotoImage(file= "IO\image\ess3.png")
image_frame.create_image(100, 100, image = logo_img)



# AnchorPane equivalent in Tkinter
anchor_pane = tk.Frame(root, width=251, height=276, background="#4A1985")
anchor_pane.place(x=55, y=64)

# Labels and other widgets inside the AnchorPane
label_month = tk.Label(anchor_pane, text="Mês:", font=("Helvetica", 21), bg="#4A1985")
label_month.place(x=29, y=14, width=54, height=31)

label_day1 = tk.Label(anchor_pane, text="Dia:", font=("Helvetica", 21), bg="#4A1985")
label_day1.place(x=25, y=45, width=53, height=25)

label_day2 = tk.Label(anchor_pane, text="Dia:", font=("Helvetica", 21),bg="#4A1985")
label_day2.place(x=22, y=141, width=53, height=25)

label_finura = tk.Label(anchor_pane, text="Finura:", font=("Helvetica", 21),bg="#4A1985")
label_finura.place(x=20, y=182, width=90, height=31)

label_agulha = tk.Label(anchor_pane, text="Agulha:", font=("Helvetica", 21),bg="#4A1985")
label_agulha.place(x=19, y=225, width=95, height=31)

#change for radio
combo_setor = ttk.Combobox(anchor_pane, values=["Raschell", "Jacquard", "ketten"], font=("Helvetica", 14))
combo_setor.place(x=21, y=92, width=87, height=25)
combo_setor.set("Setor")

combo_turno = ttk.Combobox(anchor_pane, values=["TA", "TB", "TC"], font=("Helvetica", 14))
combo_turno.place(x=142, y=92, width=87, height=25)
combo_turno.set("Turno")

month = tk.Entry(anchor_pane, font=("Helvetica", 14))
month.place(x=89, y=17, width=45, height=25)

day1 = tk.Entry(anchor_pane, font=("Helvetica", 14))
day1.place(x=89, y=48, width=45, height=25)

text_day2 = tk.Entry(anchor_pane, font=("Helvetica", 14))
text_day2.place(x=120, y=144, width=81, height=26)

text_finura = tk.Entry(anchor_pane, font=("Helvetica", 14))
text_finura.place(x=120, y=185, width=81, height=26)

text_agulha = tk.Entry(anchor_pane, font=("Helvetica", 14))
text_agulha.place(x=120, y=228, width=81, height=26)

# Footer Label
label_footer = tk.Label(root, text="Radical dreamers aw rpg ltda", 
                        font=("Helvetica", 17), fg="#1b52a4", bg="#080121")
label_footer.place(x=682, y=777, width=349, height=45)

# AnchorPane with Buttons
button_pane = tk.Frame(root, width=334, height=114, background="#4A1985")
button_pane.place(x=55, y=352)

button_add = tk.Button(button_pane, text="Adicionar", font=("Helvetica", 18), bg="#A580CA")
button_add.place(x=120, y=14, width=109)

button_skip_turn = tk.Button(button_pane, text="Pular turno", font=("Helvetica", 18), bg="#A580CA")
button_skip_turn.place(x=6, y=67)

button_add_more = tk.Button(button_pane, text="Adicionar + ", font=("Helvetica", 18), bg="#A580CA")
button_add_more.place(x=193, y=67)

# Another AnchorPane with Labels and Buttons
info_pane = tk.Frame(root, width=749, height=138, background="#4A1985")
info_pane.place(x=395, y=14)

label_agulhas_dia = tk.Label(info_pane, text="Agulhas dia", font=("Helvetica", 18),bg="#A580CA")
label_agulhas_dia.place(x=20, y=14)

button_turno_radio = tk.Button(info_pane, text="Turno radio", font=("Helvetica", 14),bg="#A580CA")
button_turno_radio.place(x=191, y=15)

button_setor_radio = tk.Button(info_pane, text="Setor Radio", font=("Helvetica", 14),bg="#A580CA")
button_setor_radio.place(x=362, y=16)

label_total = tk.Label(info_pane, text="Total", font=("Helvetica", 18))
label_total.place(x=565, y=15)

# Labels for displaying numbers
numbers = [3975, 3975, 3975, 3975, 3975]
for i, num in enumerate(numbers):
    label_num = tk.Label(info_pane, text=str(num), font=("Helvetica", 14))
    label_num.place(x=31, y=42 + i*19)

    label_num_total = tk.Label(info_pane, text=str(num), font=("Helvetica", 14))
    label_num_total.place(x=572, y=42 + i*19)

    entry_num = tk.Entry(info_pane, font=("Helvetica", 14))
    entry_num.place(x=60, y=38 + i*19, width=40)

    entry_num_total = tk.Entry(info_pane, font=("Helvetica", 14))
    entry_num_total.place(x=624, y=36 + i*19, width=40)

# Empty AnchorPanes
empty_pane1 = tk.Frame(root, width=238, height=321, background="#D8BFD8")
empty_pane1.place(x=14, y=502)

empty_pane2 = tk.Frame(root, width=227, height=321, background="#D8BFD8")
empty_pane2.place(x=251, y=502)

# Run the application
root.mainloop()
