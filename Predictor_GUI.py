import pickle
import sklearn
from tkinter import *
from tkinter import messagebox



def predict_price():

    # Accessing our model
    with open('House_Price_Prediction.pkl', 'rb') as file:
        trained_model = pickle.load(file)

    input_values = [[float(x1.get()), float(x2.get()), float(x3.get()), int(x4.get()), float(x5.get()), float(x6.get()),
                    float(x7.get()),float(x8.get()),int(x9.get()), int(x10.get()), float(x11.get()),
                     float(x12.get()), float(x13.get())]]

    predictions = trained_model.predict(input_values)
    result = predictions[0]
    messagebox.showinfo("Predicted Pricer",
                        f"Predicted House Price in $1000:  {result}")




def main_window():
    clear_Screen()
    Label(window, text="House Price Prediction", fg="white", bg="black", font=("Times New Roman", 23, 'bold')).pack()

    label_char = {
        "font": ("Times New Roman", 10),
        "fg": "white",
        "bg": "black",
    }

    Label(window, text="Crime Rate", **label_char).pack(anchor='w', pady=(8, 3), padx=10)
    global x1
    x1 = Entry(window, textvariable=DoubleVar())
    x1.place(x=200, y=51)

    Label(window, text="Land Zoning (over 25,000 sq.ft)", **label_char).pack(anchor='w', pady=(0, 3), padx=10)
    global x2
    x2 = Entry(window, textvariable=DoubleVar())
    x2.place(x=200, y=76)

    Label(window, text="Non Retail", **label_char).pack(anchor='w', pady=(1, 3), padx=10)
    global x3
    x3 = Entry(window, textvariable=DoubleVar())
    x3.place(x=200, y=101)

    Label(window, text="River (1 for Yes/ 0 for No)", **label_char).pack(anchor='w', pady=(0, 5), padx=10)
    global x4
    x4 = Entry(window, textvariable=IntVar())
    x4.place(x=200, y=126)

    Label(window, text="NO Concentration", **label_char).pack(anchor='w', pady=(0, 5), padx=10)
    global x5
    x5 = Entry(window, textvariable=DoubleVar())
    x5.place(x=200, y=151)

    Label(window, text="Avg Rooms", **label_char).pack(anchor='w', pady=(0, 5), padx=10)
    global x6
    x6 = Entry(window, textvariable=DoubleVar())
    x6.place(x=200, y=176)

    Label(window, text="Building Age", **label_char).pack(anchor='w', pady=(0, 5), padx=10)
    global x7
    x7 = Entry(window, textvariable=DoubleVar())
    x7.place(x=200, y=201)

    Label(window, text="Distance To Work", **label_char).pack(anchor='w', pady=(0, 5), padx=10)
    global x8
    x8 = Entry(window, textvariable=DoubleVar())
    x8.place(x=200, y=226)

    Label(window, text="Radial Access (Discrete value)", **label_char).pack(anchor='w', pady=(0, 5), padx=10)
    global x9
    x9 = Entry(window, textvariable=IntVar())
    x9.place(x=200, y=251)

    Label(window, text="Tax Rate (per $10,000 of value)", **label_char).pack(anchor='w', pady=(0, 3), padx=10)
    global x10
    x10 = Entry(window, textvariable=IntVar())
    x10.place(x=200, y=276)

    Label(window, text="Pupil_Teacher_Ratio", **label_char).pack(anchor='w', pady=(0, 3), padx=10)
    global x11
    x11 = Entry(window, textvariable=DoubleVar())
    x11.place(x=200, y=301)

    Label(window, text="Black Proportion", **label_char).pack(anchor='w', pady=(0, 3), padx=10)
    global x12
    x12 = Entry(window, textvariable=DoubleVar())
    x12.place(x=200, y=326)

    Label(window, text="Lower Status", **label_char).pack(anchor='w', pady=(0, 5), padx=10)
    global x13
    x13 = Entry(window, textvariable=DoubleVar())
    x13.place(x=200, y=351)

    # Button for Predicting Price
    Button(text="Predict Price", command=predict_price, fg="red", bg='black', bd=3,
           font=("Times New Roman", 15, "bold")).pack(pady=10)

    #Button for Predicting Another House Price
    Button(text="Predict Another House", command=main_window, fg="white", bg='red', bd=3,
           font=("Times New Roman", 15, "bold")).pack(pady=8)

# Function to clear the screen
def clear_Screen():
    for widget in window.winfo_children():
        widget.destroy()
    

window = Tk()
window.title("Boston House Price Predictor")
window.geometry("600x500")
window.config(bg="black")

main_window()

window.mainloop()