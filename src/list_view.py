from tkinter import ttk, constants
from services.recycle_service import recycle_service


class ListView:
    '''this class is responsible for the list view of the app'''
    def __init__(self, root, handle_start):
        self._root = root
        self.bottle_can_entry = None
        self.cardboard_entry = None
        self.electronics_entry = None
        self.glass_entry = None
        self.metal_entry = None
        self.plastic_entry = None
        self.paper_entry = None
        self.batteries_entry = None
        self.clothes_entry = None
        self._handle_start = handle_start
        self._frame = None
        self._initialize()

    def pack(self):
        '''pack the frame'''
        self._frame.pack(fill=constants.X)

    def destroy(self):
        '''destroy the frame'''
        self._frame.destroy()

    def add_to_recycle(self, material):
        '''update selected material with selected amount'''
        if material == "bottles_cans":
            amount = self.bottle_can_entry.get()
        elif material == "cardboard":
            amount = self.cardboard_entry.get()
        elif material == "electronics":
            amount = self.electronics_entry.get()
        elif material == "glass":
            amount = self.glass_entry.get()
        elif material == "metal":
            amount = self.metal_entry.get()
        elif material == "plastic":
            amount = self.plastic_entry.get()
        elif material == "paper":
            amount = self.paper_entry.get()
        elif material == "batteries":
            amount = self.batteries_entry.get()
        elif material == "clothes":
            amount = self.clothes_entry.get()
        recycle_service.recycle_list_update(amount, material)
        self._handle_start()


    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        label = ttk.Label(master=self._frame, text="Recycling list")

        bottle_can_label = ttk.Label(
            master=self._frame, text="Bottles and cans recycled:")
        bottle_can_amount = ttk.Label(
            master=self._frame, text=recycle_service.recycle_list()[0])
        self.bottle_can_entry = ttk.Entry(master=self._frame, width=4)
        bottle_can_button = ttk.Button(
            master=self._frame, text="Add more", command=lambda: self.add_to_recycle("bottles_cans"))

        cardboard_label = ttk.Label(
            master=self._frame, text="Cardboard recycled:")
        cardboard_amount = ttk.Label(
            master=self._frame, text=(recycle_service.recycle_list()[1], "square", "meters"))
        self.cardboard_entry = ttk.Entry(master=self._frame, width=4)
        cardboard_button = ttk.Button(
            master=self._frame, text="Add more", command=lambda: self.add_to_recycle("cardboard"))

        electronics_label = ttk.Label(
            master=self._frame, text="Electronics recycled:")
        electronics_amount = ttk.Label(
            master=self._frame, text=(recycle_service.recycle_list()[2], "kilograms"))
        self.electronics_entry = ttk.Entry(master=self._frame, width=4)
        electronics_button = ttk.Button(
            master=self._frame, text="Add more", command=lambda: self.add_to_recycle("electronics"))

        glass_label = ttk.Label(master=self._frame, text="Glass recycled:")
        glass_amount = ttk.Label(
            master=self._frame, text=(recycle_service.recycle_list()[3], "kilograms"))
        self.glass_entry = ttk.Entry(master=self._frame, width=4)
        glass_button = ttk.Button(
            master=self._frame, text="Add more", command=lambda: self.add_to_recycle("glass"))

        metal_label = ttk.Label(master=self._frame, text="Metal recycled:")
        metal_amount = ttk.Label(
            master=self._frame, text=(recycle_service.recycle_list()[4], "kilograms"))
        self.metal_entry = ttk.Entry(master=self._frame, width=4)
        metal_button = ttk.Button(
            master=self._frame, text="Add more", command=lambda: self.add_to_recycle("metal"))

        plastic_label = ttk.Label(master=self._frame, text="Plastic recycled:")
        plastic_amount = ttk.Label(
            master=self._frame, text=(recycle_service.recycle_list()[5], "kilograms"))
        self.plastic_entry = ttk.Entry(master=self._frame, width=4)
        plastic_button = ttk.Button(
            master=self._frame, text="Add more", command=lambda: self.add_to_recycle("plastic"))

        paper_label = ttk.Label(master=self._frame, text="Paper recycled:")
        paper_amount = ttk.Label(
            master=self._frame, text=(recycle_service.recycle_list()[6], "kilograms"))
        self.paper_entry = ttk.Entry(master=self._frame, width=4)
        paper_button = ttk.Button(
            master=self._frame, text="Add more", command=lambda: self.add_to_recycle("paper"))

        batteries_label = ttk.Label(
            master=self._frame, text="Batteries recycled:")
        batteries_amount = ttk.Label(
            master=self._frame, text=recycle_service.recycle_list()[7])
        self.batteries_entry = ttk.Entry(master=self._frame, width=4)
        batteries_button = ttk.Button(
            master=self._frame, text="Add more", command=lambda: self.add_to_recycle("batteries"))

        clothes_label = ttk.Label(master=self._frame, text="Clothes recycled:")
        clothes_amount = ttk.Label(
            master=self._frame, text=recycle_service.recycle_list()[8])
        self.clothes_entry = ttk.Entry(master=self._frame, width=4)
        clothes_button = ttk.Button(
            master=self._frame, text="Add more", command=lambda: self.add_to_recycle("clothes"))

        button = ttk.Button(master=self._frame, text="Logout",
                            command=self._handle_start)

        label.grid(row=0, column=0)

        bottle_can_label.grid(row=1, column=0)
        bottle_can_amount.grid(row=1, column=1)
        self.bottle_can_entry.grid(row=1, column=2)
        bottle_can_button.grid(row=1, column=3)

        cardboard_label.grid(row=2, column=0)
        cardboard_amount.grid(row=2, column=1)
        self.cardboard_entry.grid(row=2, column=2)
        cardboard_button.grid(row=2, column=3)

        electronics_label.grid(row=3, column=0)
        electronics_amount.grid(row=3, column=1)
        self.electronics_entry.grid(row=3, column=2)
        electronics_button.grid(row=3, column=3)

        glass_label.grid(row=4, column=0)
        glass_amount.grid(row=4, column=1)
        self.glass_entry.grid(row=4, column=2)
        glass_button.grid(row=4, column=3)

        metal_label.grid(row=5, column=0)
        metal_amount.grid(row=5, column=1)
        self.metal_entry.grid(row=5, column=2)
        metal_button.grid(row=5, column=3)

        plastic_label.grid(row=6, column=0)
        plastic_amount.grid(row=6, column=1)
        self.plastic_entry.grid(row=6, column=2)
        plastic_button.grid(row=6, column=3)

        paper_label.grid(row=7, column=0)
        paper_amount.grid(row=7, column=1)
        self.paper_entry.grid(row=7, column=2)
        paper_button.grid(row=7, column=3)

        batteries_label.grid(row=8, column=0)
        batteries_amount.grid(row=8, column=1)
        self.batteries_entry.grid(row=8, column=2)
        batteries_button.grid(row=8, column=3)

        clothes_label.grid(row=9, column=0)
        clothes_amount.grid(row=9, column=1)
        self.clothes_entry.grid(row=9, column=2)
        clothes_button.grid(row=9, column=3)

        button.grid()
