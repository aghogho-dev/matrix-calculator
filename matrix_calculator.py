import tkinter as tk
from tkinter import ttk
import numpy as np
import random
import time


class MatrixCaculator:

    def __init__(self, root):

        self.root = root
        self.root.title("Matrix Calculator")
        self.root.geometry("350x250")
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)

        self.font_label = ("Rockwell", 12)
        self.font_item = ("Verdana", 10)

        mainframe = tk.Frame(self.root)
        mainframe.grid()

        operations = ["Add", "Subtract", "Scalar Multiply",
                      "Matrix Multiply", "Inverse", "Determinant",
                      "Transpose", "2-Norm"
                      ]
        
        main_label = ttk.Label(mainframe, text="Select Operation:", font=self.font_label)
        main_label.grid(row=0, column=1, sticky=(tk.W, tk.E), padx=1, pady=1)

        self.combobox = ttk.Combobox(mainframe, value=operations, font=self.font_item)
        self.combobox.grid(row=1, column=1, sticky=(tk.N, tk.S, tk.E, tk.W), padx=1, pady=1)

        self.invalid = tk.StringVar()
        invalid_label = ttk.Label(mainframe, textvariable=self.invalid, font=self.font_label, foreground="red")
        invalid_label.grid(row=2, column=1, sticky=tk.W, padx=1, pady=1)

        go_btn = ttk.Button(mainframe, text="Go", command=self.get_combobox_operation)
        go_btn.grid(row=3, column=1, sticky=tk.E, padx=1, pady=1)


        style = ttk.Style()
        style.configure("Custom.TButton", font=self.font_label)
        go_btn.configure(style="Custom.TButton")


    def get_combobox_operation(self):

        selected_operation = self.combobox.get()


        options = {
            "Add": self.get_add, 
            "Subtract": self.get_subtract, 
            "Scalar Multiply": self.get_scalar_multiply,
            "Matrix Multiply": self.get_matrix_multiply, 
            "Inverse": self.get_inverse, 
            "Determinant": self.get_determinant,
            "Transpose": self.get_transpose, 
            "2-Norm": self.get_2_norm 
        }

        get_function = options.get(selected_operation, None)

        if get_function is None:

            self.invalid.set("invalid")

        else:
            self.invalid.set("")
            get_function(selected_operation)
            

    def get_add(self, selected_operation):
        
        window = tk.Toplevel(self.root)
        window.title(f"{selected_operation} Operation")
        window.geometry("800x200")
        window.rowconfigure(0, weight=1)
        window.columnconfigure(0, weight=1)
        
        frame = ttk.Frame(window)
        frame.grid()

        self.first_matrix = tk.Text(frame, width=28, height=6, background="lightgray", font=self.font_item)
        self.first_matrix.grid(row=1, column=0, padx=1, pady=1, sticky=(tk.N, tk.S, tk.E, tk.W))

        plus_label = ttk.Label(frame, text="+", font=self.font_label)
        plus_label.grid(row=1, column=2, sticky=(tk.W, tk.E), padx=1, pady=1)

        self.second_matrix = tk.Text(frame, width=28, height=6, background="lightgray", font=self.font_item)
        self.second_matrix.grid(row=1, column=3, padx=1, pady=1, sticky=(tk.N, tk.S, tk.E, tk.W))

        equals_label = ttk.Label(frame, text="=", font=self.font_label)
        equals_label.grid(row=1, column=4, sticky=(tk.W, tk.E), padx=1, pady=1)

        self.answer_matrix = tk.Text(frame, width=28, height=6, background="lightblue", font=self.font_item)
        self.answer_matrix.grid(row=1, column=5, padx=1, pady=1, sticky=(tk.N, tk.S, tk.E, tk.W))
        
        self.invalid_add = tk.StringVar()
        invalid_label = ttk.Label(frame, textvariable=self.invalid_add, font=self.font_label, foreground="red")
        invalid_label.grid(row=2, column=0, sticky=tk.W, padx=1, pady=1)

        self.invalid_add1 = tk.StringVar()
        invalid_label1 = ttk.Label(frame, textvariable=self.invalid_add1, font=self.font_label, foreground="red")
        invalid_label1.grid(row=2, column=3, sticky=tk.W, padx=1, pady=1)

        self.invalid_add2 = tk.StringVar()
        invalid_label2 = ttk.Label(frame, textvariable=self.invalid_add2, font=self.font_label, foreground="red")
        invalid_label2.grid(row=2, column=5, sticky=tk.W, padx=1, pady=1)


        add_btn = ttk.Button(frame, text="Add", command=self.add_matrix)
        add_btn.grid(row=3, column=5, padx=1, pady=1, sticky=tk.E)
        add_btn.configure(style="Custom.TButton")


    def add_matrix(self):
        
        first_matrix_value = self.first_matrix.get("1.0", "end-1c")
        first_matrix_list = [i.split() for i in first_matrix_value.split("\n") if i]
        try:
            nrows1, ncols1 = len(first_matrix_list), len(random.choice(first_matrix_list))
            first_matrix_list = [float(i) for j in first_matrix_list for i in j]
            self.invalid_add.set("")
        except ValueError:
            self.invalid_add.set("There is an invalid entry")

        second_matrix_value = self.second_matrix.get("1.0", "end-1c")
        second_matrix_list = [i.split() for i in second_matrix_value.split("\n") if i]
        
        try:
            nrows2, ncols2 = len(second_matrix_list), len(random.choice(second_matrix_list))
            second_matrix_list = [float(i) for j in second_matrix_list for i in j]
            self.invalid_add1.set("")
        except ValueError:
            self.invalid_add1.set("There is an invalid entry")

        first_matrix = np.array(first_matrix_list).reshape(nrows1, ncols1)
        second_matrix = np.array(second_matrix_list).reshape(nrows2, ncols2)

        if first_matrix.shape != second_matrix.shape:
            self.invalid_add2.set(f"{first_matrix.shape} != {second_matrix.shape}")
        else:
            self.invalid_add2.set("")
            add_matrix = np.add(first_matrix, second_matrix)
            
            ans_str = "\n".join([" ".join(map(str, row)) for row in add_matrix])
            self.answer_matrix.delete("1.0", tk.END)
            self.answer_matrix.insert(tk.END, ans_str)

    def get_subtract(self, selected_operation):

        window = tk.Toplevel(self.root)
        window.title(f"{selected_operation} Operation")
        window.geometry("800x200")
        window.rowconfigure(0, weight=1)
        window.columnconfigure(0, weight=1)
        
        frame = ttk.Frame(window)
        frame.grid()

        self.first_matrix = tk.Text(frame, width=28, height=6, background="lightgray", font=self.font_item)
        self.first_matrix.grid(row=1, column=0, padx=1, pady=1, sticky=(tk.N, tk.S, tk.E, tk.W))

        sub_label = ttk.Label(frame, text="-", font=self.font_label)
        sub_label.grid(row=1, column=2, sticky=(tk.W, tk.E), padx=1, pady=1)

        self.second_matrix = tk.Text(frame, width=28, height=6, background="lightgray", font=self.font_item)
        self.second_matrix.grid(row=1, column=3, padx=1, pady=1, sticky=(tk.N, tk.S, tk.E, tk.W))

        equals_label = ttk.Label(frame, text="=", font=self.font_label)
        equals_label.grid(row=1, column=4, sticky=(tk.W, tk.E), padx=1, pady=1)

        self.answer_matrix = tk.Text(frame, width=28, height=6, background="lightblue", font=self.font_item)
        self.answer_matrix.grid(row=1, column=5, padx=1, pady=1, sticky=(tk.N, tk.S, tk.E, tk.W))
        
        self.invalid_sub = tk.StringVar()
        invalid_label = ttk.Label(frame, textvariable=self.invalid_sub, font=self.font_label, foreground="red")
        invalid_label.grid(row=2, column=0, sticky=tk.W, padx=1, pady=1)

        self.invalid_sub1 = tk.StringVar()
        invalid_label1 = ttk.Label(frame, textvariable=self.invalid_sub1, font=self.font_label, foreground="red")
        invalid_label1.grid(row=2, column=3, sticky=tk.W, padx=1, pady=1)

        self.invalid_sub2 = tk.StringVar()
        invalid_label2 = ttk.Label(frame, textvariable=self.invalid_sub2, font=self.font_label, foreground="red")
        invalid_label2.grid(row=2, column=5, sticky=tk.W, padx=1, pady=1)

        sub_btn = ttk.Button(frame, text="Subtract", command=self.subtract_matrix)
        sub_btn.grid(row=3, column=5, padx=1, pady=1, sticky=tk.E)
        sub_btn.configure(style="Custom.TButton")

    def subtract_matrix(self):

        first_matrix_value = self.first_matrix.get("1.0", "end-1c")
        first_matrix_list = [i.split() for i in first_matrix_value.split("\n") if i]
        try:
            nrows1, ncols1 = len(first_matrix_list), len(random.choice(first_matrix_list))
            first_matrix_list = [float(i) for j in first_matrix_list for i in j]
            self.invalid_sub.set("")
        except ValueError:
            self.invalid_sub.set("There is an invalid entry")

        second_matrix_value = self.second_matrix.get("1.0", "end-1c")
        second_matrix_list = [i.split() for i in second_matrix_value.split("\n") if i]
        
        try:
            nrows2, ncols2 = len(second_matrix_list), len(random.choice(second_matrix_list))
            second_matrix_list = [float(i) for j in second_matrix_list for i in j]
            self.invalid_sub1.set("")
        except ValueError:
            self.invalid_sub1.set("There is an invalid entry")

        first_matrix = np.array(first_matrix_list).reshape(nrows1, ncols1)
        second_matrix = np.array(second_matrix_list).reshape(nrows2, ncols2)

        if first_matrix.shape != second_matrix.shape:
            self.invalid_sub2.set(f"{first_matrix.shape} != {second_matrix.shape}")
        else:
            self.invalid_sub2.set("")
            add_matrix = np.subtract(first_matrix, second_matrix)
            
            ans_str = "\n".join([" ".join(map(str, row)) for row in add_matrix])
            self.answer_matrix.delete("1.0", tk.END)
            self.answer_matrix.insert(tk.END, ans_str)

    def get_scalar_multiply(self, selected_operation):

        window = tk.Toplevel(self.root)
        window.title(f"{selected_operation} Operation")
        window.geometry("800x200")
        window.rowconfigure(0, weight=1)
        window.columnconfigure(0, weight=1)
        
        frame = ttk.Frame(window)
        frame.grid()

        self.k_entry = tk.Entry(frame, width=10, background="greenyellow", font=self.font_item, justify="center")
        self.k_entry.grid(row=1, column=0, padx=1, pady=1, sticky=(tk.N, tk.S, tk.E, tk.W))

        kmul_label = ttk.Label(frame, text="x", font=self.font_label)
        kmul_label.grid(row=1, column=2, sticky=(tk.W, tk.E), padx=1, pady=1)

        self.second_matrix = tk.Text(frame, width=28, height=6, background="lightgray", font=self.font_item)
        self.second_matrix.grid(row=1, column=3, padx=1, pady=1, sticky=(tk.N, tk.S, tk.E, tk.W))

        equals_label = ttk.Label(frame, text="=", font=self.font_label)
        equals_label.grid(row=1, column=4, sticky=(tk.W, tk.E), padx=1, pady=1)

        self.answer_matrix = tk.Text(frame, width=28, height=6, background="lightblue", font=self.font_item)
        self.answer_matrix.grid(row=1, column=5, padx=1, pady=1, sticky=(tk.N, tk.S, tk.E, tk.W))

        self.invalid_kmul = tk.StringVar()
        invalid_label = ttk.Label(frame, textvariable=self.invalid_kmul, font=self.font_label, foreground="red")
        invalid_label.grid(row=2, column=0, sticky=tk.W, padx=1, pady=1)

        self.invalid_kmul1 = tk.StringVar()
        invalid_label1 = ttk.Label(frame, textvariable=self.invalid_kmul1, font=self.font_label, foreground="red")
        invalid_label1.grid(row=2, column=3, sticky=tk.W, padx=1, pady=1)

        self.invalid_kmul2 = tk.StringVar()
        invalid_label2 = ttk.Label(frame, textvariable=self.invalid_kmul2, font=self.font_label, foreground="red")
        invalid_label2.grid(row=2, column=5, sticky=tk.W, padx=1, pady=1)

        kmul_btn = ttk.Button(frame, text="Multiply", command=self.scalar_multiply)
        kmul_btn.grid(row=3, column=5, padx=1, pady=1, sticky=tk.E)
        kmul_btn.configure(style="Custom.TButton")

    def scalar_multiply(self):

        k_value = self.k_entry.get()
        try:
            k_value = float(k_value.strip())
            self.invalid_kmul.set("")
        except ValueError:
            self.invalid_kmul.set("Invalid entry")

        second_matrix_value = self.second_matrix.get("1.0", "end-1c")
        second_matrix_list = [i.split() for i in second_matrix_value.split("\n") if i]
        
        try:
            nrows2, ncols2 = len(second_matrix_list), len(random.choice(second_matrix_list))
            second_matrix_list = [float(i) for j in second_matrix_list for i in j]
            self.invalid_kmul1.set("")
        except ValueError:
            self.invalid_kmul1.set("There is an invalid entry")

        second_matrix = np.array(second_matrix_list).reshape(nrows2, ncols2)
        
        add_matrix = k_value * second_matrix
            
        ans_str = "\n".join([" ".join(map(str, row)) for row in add_matrix])
        self.answer_matrix.delete("1.0", tk.END)
        self.answer_matrix.insert(tk.END, ans_str)


    def get_matrix_multiply(self, selected_operation):
        
        window = tk.Toplevel(self.root)
        window.title(f"{selected_operation} Operation")
        window.geometry("800x200")
        window.rowconfigure(0, weight=1)
        window.columnconfigure(0, weight=1)
        
        frame = ttk.Frame(window)
        frame.grid()

        self.first_matrix = tk.Text(frame, width=28, height=6, background="lightgray", font=self.font_item)
        self.first_matrix.grid(row=1, column=0, padx=1, pady=1, sticky=(tk.N, tk.S, tk.E, tk.W))

        mul_label = ttk.Label(frame, text="x", font=self.font_label)
        mul_label.grid(row=1, column=2, sticky=(tk.W, tk.E), padx=1, pady=1)

        self.second_matrix = tk.Text(frame, width=28, height=6, background="lightgray", font=self.font_item)
        self.second_matrix.grid(row=1, column=3, padx=1, pady=1, sticky=(tk.N, tk.S, tk.E, tk.W))

        equals_label = ttk.Label(frame, text="=", font=self.font_label)
        equals_label.grid(row=1, column=4, sticky=(tk.W, tk.E), padx=1, pady=1)

        self.answer_matrix = tk.Text(frame, width=28, height=6, background="lightblue", font=self.font_item)
        self.answer_matrix.grid(row=1, column=5, padx=1, pady=1, sticky=(tk.N, tk.S, tk.E, tk.W))
        
        self.invalid_mul = tk.StringVar()
        invalid_label = ttk.Label(frame, textvariable=self.invalid_mul, font=self.font_label, foreground="red")
        invalid_label.grid(row=2, column=0, sticky=tk.W, padx=1, pady=1)

        self.invalid_mul1 = tk.StringVar()
        invalid_label1 = ttk.Label(frame, textvariable=self.invalid_mul1, font=self.font_label, foreground="red")
        invalid_label1.grid(row=2, column=3, sticky=tk.W, padx=1, pady=1)

        self.invalid_mul2 = tk.StringVar()
        invalid_label2 = ttk.Label(frame, textvariable=self.invalid_mul2, font=self.font_label, foreground="red")
        invalid_label2.grid(row=2, column=5, sticky=tk.W, padx=1, pady=1)


        mul_btn = ttk.Button(frame, text="Multiply", command=self.matrix_multiply)
        mul_btn.grid(row=3, column=5, padx=1, pady=1, sticky=tk.E)
        mul_btn.configure(style="Custom.TButton")

    def matrix_multiply(self):

        first_matrix_value = self.first_matrix.get("1.0", "end-1c")
        first_matrix_list = [i.split() for i in first_matrix_value.split("\n") if i]
        try:
            nrows1, ncols1 = len(first_matrix_list), len(random.choice(first_matrix_list))
            first_matrix_list = [float(i) for j in first_matrix_list for i in j]
            self.invalid_mul.set("")
        except ValueError:
            self.invalid_mul.set("There is an invalid entry")

        second_matrix_value = self.second_matrix.get("1.0", "end-1c")
        second_matrix_list = [i.split() for i in second_matrix_value.split("\n") if i]
        
        try:
            nrows2, ncols2 = len(second_matrix_list), len(random.choice(second_matrix_list))
            second_matrix_list = [float(i) for j in second_matrix_list for i in j]
            self.invalid_mul1.set("")
        except ValueError:
            self.invalid_mul1.set("There is an invalid entry")

        first_matrix = np.array(first_matrix_list).reshape(nrows1, ncols1)
        second_matrix = np.array(second_matrix_list).reshape(nrows2, ncols2)

        if first_matrix.shape[1] != second_matrix.shape[0]:
            self.invalid_mul2.set(f"First column ({first_matrix.shape[1]}) != Second row ({second_matrix.shape[0]})")
        else:
            self.invalid_mul2.set("")
            add_matrix = np.dot(first_matrix, second_matrix)
            
            ans_str = "\n".join([" ".join(map(str, row)) for row in add_matrix])
            self.answer_matrix.delete("1.0", tk.END)
            self.answer_matrix.insert(tk.END, ans_str)

    def get_inverse(self, selected_operation):
        
        window = tk.Toplevel(self.root)
        window.title(f"{selected_operation} Operation")
        window.geometry("600x200")
        window.rowconfigure(0, weight=1)
        window.columnconfigure(0, weight=1)
        
        frame = ttk.Frame(window)
        frame.grid()

        self.first_matrix = tk.Text(frame, width=28, height=6, background="lightgray", font=self.font_item)
        self.first_matrix.grid(row=1, column=0, padx=1, pady=1, sticky=(tk.N, tk.S, tk.E, tk.W))

        equals_label = ttk.Label(frame, text="=", font=self.font_label)
        equals_label.grid(row=1, column=1, sticky=(tk.W, tk.E), padx=1, pady=1)

        self.answer_matrix = tk.Text(frame, width=28, height=6, background="lightblue", font=self.font_item)
        self.answer_matrix.grid(row=1, column=3, padx=1, pady=1, sticky=(tk.N, tk.S, tk.E, tk.W))
        
        self.invalid_inv = tk.StringVar()
        invalid_label = ttk.Label(frame, textvariable=self.invalid_inv, font=self.font_label, foreground="red")
        invalid_label.grid(row=2, column=0, sticky=tk.W, padx=1, pady=1)

        self.invalid_inv2 = tk.StringVar()
        invalid_label2 = ttk.Label(frame, textvariable=self.invalid_inv2, font=self.font_label, foreground="red")
        invalid_label2.grid(row=2, column=3, sticky=tk.W, padx=1, pady=1)


        inv_btn = ttk.Button(frame, text="Inverse", command=self.matrix_inverse)
        inv_btn.grid(row=3, column=3, padx=1, pady=1, sticky=tk.E)
        inv_btn.configure(style="Custom.TButton")

    def matrix_inverse(self):
        
        first_matrix_value = self.first_matrix.get("1.0", "end-1c")
        first_matrix_list = [i.split() for i in first_matrix_value.split("\n") if i]
        try:
            nrows1, ncols1 = len(first_matrix_list), len(random.choice(first_matrix_list))
            first_matrix_list = [float(i) for j in first_matrix_list for i in j]
            self.invalid_inv.set("")
        except ValueError:
            self.invalid_inv.set("There is an invalid entry")

        first_matrix = np.array(first_matrix_list).reshape(nrows1, ncols1)

        try:
            self.invalid_inv2.set("")
            add_matrix = np.round(np.linalg.inv(first_matrix), 3)
            
            ans_str = "\n".join([" ".join(map(str, row)) for row in add_matrix])
            self.answer_matrix.delete("1.0", tk.END)
            self.answer_matrix.insert(tk.END, ans_str)

        except Exception as e:
            self.invalid_inv2.set("Cannot find inverse")

    def get_determinant(self, selected_operation):
        
        window = tk.Toplevel(self.root)
        window.title(f"{selected_operation} Operation")
        window.geometry("600x200")
        window.rowconfigure(0, weight=1)
        window.columnconfigure(0, weight=1)
        
        frame = ttk.Frame(window)
        frame.grid()

        self.first_matrix = tk.Text(frame, width=28, height=6, background="lightgray", font=self.font_item)
        self.first_matrix.grid(row=1, column=0, padx=1, pady=1, sticky=(tk.N, tk.S, tk.E, tk.W))

        equals_label = ttk.Label(frame, text="=", font=self.font_label)
        equals_label.grid(row=1, column=1, sticky=(tk.W, tk.E), padx=1, pady=1)

        self.answer_matrix = tk.Text(frame, width=28, height=6, background="lightblue", font=self.font_item)
        self.answer_matrix.grid(row=1, column=3, padx=1, pady=1, sticky=(tk.N, tk.S, tk.E, tk.W))
        
        self.invalid_det = tk.StringVar()
        invalid_label = ttk.Label(frame, textvariable=self.invalid_det, font=self.font_label, foreground="red")
        invalid_label.grid(row=2, column=0, sticky=tk.W, padx=1, pady=1)

        self.invalid_det2 = tk.StringVar()
        invalid_label2 = ttk.Label(frame, textvariable=self.invalid_det2, font=self.font_label, foreground="red")
        invalid_label2.grid(row=2, column=3, sticky=tk.W, padx=1, pady=1)

        det_btn = ttk.Button(frame, text="Determinant", command=self.matrix_determinant)
        det_btn.grid(row=3, column=3, padx=1, pady=1, sticky=tk.E)
        det_btn.configure(style="Custom.TButton")

    def matrix_determinant(self):

        first_matrix_value = self.first_matrix.get("1.0", "end-1c")
        first_matrix_list = [i.split() for i in first_matrix_value.split("\n") if i]
        try:
            nrows1, ncols1 = len(first_matrix_list), len(random.choice(first_matrix_list))
            first_matrix_list = [float(i) for j in first_matrix_list for i in j]
            self.invalid_det.set("")
        except ValueError:
            self.invalid_det.set("There is an invalid entry")

        first_matrix = np.array(first_matrix_list).reshape(nrows1, ncols1)

        if nrows1 != ncols1:
            self.invalid_det.set(f"{first_matrix.shape} must be square")
            
        else:
            try:
                self.invalid_det2.set("")
                add_matrix = np.round(np.linalg.det(first_matrix), 3)
                
                self.answer_matrix.delete("1.0", tk.END)
                self.answer_matrix.insert(tk.END, str(add_matrix))

            except Exception as e:
                self.invalid_det2.set(f"{e}")


    def get_transpose(self, selected_operation):
        
        window = tk.Toplevel(self.root)
        window.title(f"{selected_operation} Operation")
        window.geometry("600x200")
        window.rowconfigure(0, weight=1)
        window.columnconfigure(0, weight=1)
        
        frame = ttk.Frame(window)
        frame.grid()

        self.first_matrix = tk.Text(frame, width=28, height=6, background="lightgray", font=self.font_item)
        self.first_matrix.grid(row=1, column=0, padx=1, pady=1, sticky=(tk.N, tk.S, tk.E, tk.W))

        equals_label = ttk.Label(frame, text="=", font=self.font_label)
        equals_label.grid(row=1, column=1, sticky=(tk.W, tk.E), padx=1, pady=1)

        self.answer_matrix = tk.Text(frame, width=28, height=6, background="lightblue", font=self.font_item)
        self.answer_matrix.grid(row=1, column=3, padx=1, pady=1, sticky=(tk.N, tk.S, tk.E, tk.W))
        
        self.invalid_trans = tk.StringVar()
        invalid_label = ttk.Label(frame, textvariable=self.invalid_trans, font=self.font_label, foreground="red")
        invalid_label.grid(row=2, column=0, sticky=tk.W, padx=1, pady=1)

        self.invalid_trans2 = tk.StringVar()
        invalid_label2 = ttk.Label(frame, textvariable=self.invalid_trans2, font=self.font_label, foreground="red")
        invalid_label2.grid(row=2, column=3, sticky=tk.W, padx=1, pady=1)

        trans_btn = ttk.Button(frame, text="Transpose", command=self.matrix_transpose)
        trans_btn.grid(row=3, column=3, padx=1, pady=1, sticky=tk.E)
        trans_btn.configure(style="Custom.TButton")

    def matrix_transpose(self):

        first_matrix_value = self.first_matrix.get("1.0", "end-1c")
        first_matrix_list = [i.split() for i in first_matrix_value.split("\n") if i]
        try:
            nrows1, ncols1 = len(first_matrix_list), len(random.choice(first_matrix_list))
            first_matrix_list = [float(i) for j in first_matrix_list for i in j]
            self.invalid_trans.set("")
        except ValueError:
            self.invalid_trans.set("There is an invalid entry")

        first_matrix = np.array(first_matrix_list).reshape(nrows1, ncols1)

        try:
            self.invalid_trans2.set("")
            add_matrix = np.transpose(first_matrix)

            ans_str = "\n".join([" ".join(map(str, row)) for row in add_matrix])
            
            self.answer_matrix.delete("1.0", tk.END)
            self.answer_matrix.insert(tk.END, str(ans_str))

        except Exception as e:
            self.invalid_trans2.set(f"{e}")

    def get_2_norm(self, selected_operation):
        
        window = tk.Toplevel(self.root)
        window.title(f"{selected_operation} Operation")
        window.geometry("600x200")
        window.rowconfigure(0, weight=1)
        window.columnconfigure(0, weight=1)
        
        frame = ttk.Frame(window)
        frame.grid()

        self.first_matrix = tk.Text(frame, width=28, height=6, background="lightgray", font=self.font_item)
        self.first_matrix.grid(row=1, column=0, padx=1, pady=1, sticky=(tk.N, tk.S, tk.E, tk.W))

        equals_label = ttk.Label(frame, text="=", font=self.font_label)
        equals_label.grid(row=1, column=1, sticky=(tk.W, tk.E), padx=1, pady=1)

        self.answer_matrix = tk.Text(frame, width=28, height=6, background="lightblue", font=self.font_item)
        self.answer_matrix.grid(row=1, column=3, padx=1, pady=1, sticky=(tk.N, tk.S, tk.E, tk.W))
        
        self.invalid_norm = tk.StringVar()
        invalid_label = ttk.Label(frame, textvariable=self.invalid_norm, font=self.font_label, foreground="red")
        invalid_label.grid(row=2, column=0, sticky=tk.W, padx=1, pady=1)

        self.invalid_norm2 = tk.StringVar()
        invalid_label2 = ttk.Label(frame, textvariable=self.invalid_norm2, font=self.font_label, foreground="red")
        invalid_label2.grid(row=2, column=3, sticky=tk.W, padx=1, pady=1)

        norm_btn = ttk.Button(frame, text="2-Norm", command=self.matrix_2_norm)
        norm_btn.grid(row=3, column=3, padx=1, pady=1, sticky=tk.E)
        norm_btn.configure(style="Custom.TButton")

    def matrix_2_norm(self):

        first_matrix_value = self.first_matrix.get("1.0", "end-1c")
        first_matrix_list = [i.split() for i in first_matrix_value.split("\n") if i]
        try:
            nrows1, ncols1 = len(first_matrix_list), len(random.choice(first_matrix_list))
            first_matrix_list = [float(i) for j in first_matrix_list for i in j]
            self.invalid_norm.set("")
        except ValueError:
            self.invalid_norm.set("There is an invalid entry")

        first_matrix = np.array(first_matrix_list).reshape(nrows1, ncols1)

        try:
            self.invalid_norm2.set("")
            add_matrix = np.round(np.linalg.norm(first_matrix), 3)
            
            self.answer_matrix.delete("1.0", tk.END)
            self.answer_matrix.insert(tk.END, str(add_matrix))

        except Exception as e:
            self.invalid_norm2.set(f"{e}")


root = tk.Tk()
MatrixCaculator(root)
root.mainloop()
