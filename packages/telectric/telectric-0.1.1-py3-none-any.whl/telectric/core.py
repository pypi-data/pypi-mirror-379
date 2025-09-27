import math
import tkinter as tk
from tkinter import ttk

# توابع محاسباتی بدون ولتاژ

def power(current=None, voltage=None, resistance=None):
    if current is not None and voltage is not None:
        # P = I * V
        return current * voltage
    elif current is not None and resistance is not None:
        # P = I² * R
        return current ** 2 * resistance
    elif voltage is not None and resistance is not None:
        # P = V² / R
        return voltage ** 2 / resistance
    else:
        raise ValueError("برای محاسبه توان باید دو مقدار از (current, voltage, resistance) داده شود.")

def current(power=None, voltage=None, resistance=None):
    if power is not None and voltage is not None:
        # I = P / V
        return power / voltage
    elif voltage is not None and resistance is not None:
        # I = V / R
        return voltage / resistance
    elif power is not None and resistance is not None:
        # I = √(P / R)
        return math.sqrt(power / resistance)
    else:
        raise ValueError("برای محاسبه جریان باید دو مقدار از (power, voltage, resistance) داده شود.")

def resistance(voltage=None, current=None, power=None):
    if voltage is not None and current is not None:
        # R = V / I
        return voltage / current
    elif voltage is not None and power is not None:
        # R = V² / P
        return voltage ** 2 / power
    elif power is not None and current is not None:
        # R = P / I²
        return power / (current ** 2)
    else:
        raise ValueError("برای محاسبه مقاومت باید دو مقدار از (voltage, current, power) داده شود.")

# تابع برای راه‌اندازی رابط گرافیکی
def init():
    root = tk.Tk()
    root.title("TElectric - Electrical Calculator")
    root.geometry("500x400")

    # نمایش عنوان
    title_label = ttk.Label(root, text="TElectric Calculator", font=("Arial", 16))
    title_label.pack(pady=20)

    # فریم برای وارد کردن مقادیر
    input_frame = ttk.Frame(root)
    input_frame.pack(pady=10)

    # مقادیر ورودی برای ولتاژ
    current_label = ttk.Label(input_frame, text="Current (I) [A]:")
    current_label.grid(row=0, column=0)
    current_entry = ttk.Entry(input_frame)
    current_entry.grid(row=0, column=1)

    resistance_label = ttk.Label(input_frame, text="Resistance (R) [Ω]:")
    resistance_label.grid(row=1, column=0)
    resistance_entry = ttk.Entry(input_frame)
    resistance_entry.grid(row=1, column=1)

    power_label = ttk.Label(input_frame, text="Power (P) [W]:")
    power_label.grid(row=2, column=0)
    power_entry = ttk.Entry(input_frame)
    power_entry.grid(row=2, column=1)

    # نمایش نتیجه
    result_label = ttk.Label(root, text="Result: ", font=("Arial", 12))
    result_label.pack(pady=20)

    # تابع محاسبه و نمایش نتیجه
    def calculate():
        try:
            I = float(current_entry.get()) if current_entry.get() else None
            R = float(resistance_entry.get()) if resistance_entry.get() else None
            P = float(power_entry.get()) if power_entry.get() else None

            # ابتدا تلاش می‌کنیم تا توان رو محاسبه کنیم
            if P is None and I is not None and R is not None:
                P = power(current=I, resistance=R)
                result_label.config(text=f"Power (P): {P:.2f} W")

            # اگر توان داده شده نباشه، جریان رو محاسبه می‌کنیم
            elif I is None and P is not None and R is not None:
                I = current(power=P, resistance=R)
                result_label.config(text=f"Current (I): {I:.2f} A")

            # اگر جریان داده شده نباشه، مقاومت رو محاسبه می‌کنیم
            elif R is None and P is not None and I is not None:
                R = resistance(power=P, current=I)
                result_label.config(text=f"Resistance (R): {R:.2f} Ω")
            else:
                result_label.config(text="Error: Please enter two values for calculation.")

        except Exception as e:
            result_label.config(text=f"Error: {e}")

    # دکمه برای محاسبه
    calc_btn = ttk.Button(root, text="Calculate", command=calculate)
    calc_btn.pack(pady=10)

    root.mainloop()
