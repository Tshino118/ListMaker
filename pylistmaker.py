import tkinter as tk
import sqlite3 as sql3
import signal
import sys
import setup

class Frame(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        path=rf'./database.sqlite'
        self.conn= sql3.connect(path)
        self.cur = self.conn.cursor()
        self.cur.execute("select * from English")
        tables=self.cur.fetchall()

        self.master.title("ListMaker")
        self.width=900
        self.height=400
        self.create_widgets(tables)
        
    def create_widgets(self,tables):
        entry=tk.Entry
        button=tk.Button
        self.text1 = tk.StringVar()
        self.text1.set(f'result:{tables}')
        self.label1 = tk.Label(textvariable=self.text1)
        self.label1.grid(row=1, column=0, columnspan=10, padx=5, pady=5,sticky=tk.W+tk.N )
        self.entry1 = entry(width=15)
        self.entry1.grid(row=0, column=0, columnspan=2, padx=5, pady=5,sticky=tk.W)
        self.entry2 = entry(width=15)
        self.entry2.grid(row=0, column=3, columnspan=4, padx=5, pady=5,sticky=tk.W)
        self.commit = button(text="Commit", fg="blue",command=self.Button1Click)
        self.commit.grid(row=0, column=8, columnspan=2, padx=5, pady=5,sticky=tk.W)

    def Button1Click(self): #ボタンが押された時に呼ばれるメソッド
        if self.entry1.get() != "" and  self.entry2.get()!= "":
            out=self.Commit(self.entry1.get(),self.entry2.get())
            self.text1.set(f"result:{out}") #計算結果をentry3に表示

    def Commit(self,sentence,description):
        try:
            self.cur.execute(
                f"""INSERT INTO 
                    English(sentence, description)
                    VALUES ("{sentence}","{description}")
                """
            )
            self.conn.commit()
            self.cur.execute("select * from English")
            tables=self.cur.fetchall()
            return f'{sentence} is inserted\n{tables}'

        except sql3.Error as e:
            return f'insert error: {e.args[0]}'

    def CloseDB(self):
        self.conn.close()
        return 'commited.'
        
if __name__ == '__main__':
    sig_handler=lambda signum,frame : sys.exit(1)
    signal.signal(signal.SIGTERM, sig_handler)
    try:
        f = Frame()
        f.mainloop()
    finally:
        signal.signal(signal.SIGTERM, signal.SIG_IGN)
        signal.signal(signal.SIGINT, signal.SIG_IGN)
        f.CloseDB()
        signal.signal(signal.SIGTERM, signal.SIG_DFL)
        signal.signal(signal.SIGINT, signal.SIG_DFL)