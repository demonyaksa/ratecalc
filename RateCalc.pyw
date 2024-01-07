import tkinter as tk

def calculate_compound_interest():
    try:
        principal = float(entry_principal.get())
        rate = float(entry_rate.get()) / 100
        times = int(entry_times.get())

        compound_interest = principal * (1 + rate) ** times - principal
        total_amount = principal + compound_interest

        result_label.config(text=f"复利总额：{compound_interest:.2f} 元\n总金额：{total_amount:.2f} 元")
    except ValueError:
        result_label.config(text="请输入有效的数字")

# 创建主窗口
root = tk.Tk()
root.title("复利计算器")

# 获取屏幕宽度和高度
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# 设置窗口大小和位置
window_width = 300
window_height = 200
x_position = (screen_width - window_width) // 2
y_position = (screen_height - window_height) // 2
root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

# 创建输入框和标签
label_principal = tk.Label(root, text="金额（元）：")
entry_principal = tk.Entry(root)
label_rate = tk.Label(root, text="复利百分比：")
entry_rate = tk.Entry(root)
label_times = tk.Label(root, text="次数：")
entry_times = tk.Entry(root)

# 创建计算按钮
calculate_button = tk.Button(root, text="计算", command=calculate_compound_interest)

# 创建结果标签
result_label = tk.Label(root, text="")

# 布局
label_principal.grid(row=0, column=0, padx=10, pady=5)
entry_principal.grid(row=0, column=1, padx=10, pady=5)
label_rate.grid(row=1, column=0, padx=10, pady=5)
entry_rate.grid(row=1, column=1, padx=10, pady=5)
label_times.grid(row=2, column=0, padx=10, pady=5)
entry_times.grid(row=2, column=1, padx=10, pady=5)
calculate_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)
result_label.grid(row=4, column=0, columnspan=2, padx=10, pady=5)

root.mainloop()
