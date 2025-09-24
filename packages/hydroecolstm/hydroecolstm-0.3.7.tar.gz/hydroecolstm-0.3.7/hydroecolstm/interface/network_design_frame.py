
import customtkinter as ctk
import tkinter as tk
from CTkToolTip import CTkToolTip
from PIL import Image
from pathlib import Path
from ray import tune

class NetworkDesignFrame(ctk.CTkScrollableFrame):
    def __init__(self, container=None, config=None, globalData=None):
        super().__init__(container)
        
        # setup the grid layout manager
        self.config = config
        self.globalData = globalData
        self.columnconfigure((0), weight=1)
        self.__create_widgets()

        
    # create widgets for sidebar frame
    def __create_widgets(self): 
        
        # create tabs
        self.tabview = ctk.CTkTabview(master=self, width = 750, 
                                      border_width=1.5,
                                      fg_color = "transparent")
        self.tabview.pack(fill='both',expand=1)
        self.tabview.add("1. Model class")
        self.tabview.tab("1. Model class").grid_columnconfigure((0,1), weight=1)
        self.tabview.tab("1. Model class").rowconfigure((0,1,2,3,4,5,6,7), weight=1)
        self.tabview.add("2. Model head")
        self.tabview.tab("2. Model head").grid_columnconfigure((0), weight=1)
        
        self.ray_tooltip = ('Or input the tune Search Space API command, ' +
                            'e.g., tune.grid_search([20, 30]). Please see: ' + 
                            'https://docs.ray.io/en/latest/tune/api/search_space.html \n'+
                            'IMPORTANT: Box color interpretation: \n ' +
                            'wrong input = light rose  \n ' +
                            'correct input = light green color')
        
        ctk.CTkButton(master=self,  anchor='w', fg_color='gray',
                      text="Show model head and classes",
                      command=self.__show_model_head_class).pack(anchor="e", pady = 10)
        
        self.error_label = ctk.CTkLabel(master=self,  anchor='w', text=" ",
                                        fg_color='transparent', text_color = "red")
        self.error_label.pack(anchor="w", padx = 10)
        
        # ----------------------------------------------------------2. Model heads
        self.intro_label = ctk.CTkLabel(self.tabview.tab("2. Model head"), 
                                        text="1. Select model head")
        self.intro_label.grid(row=0, column=0, padx = 10, pady=(5,5), sticky="w")
        
        self.model_head_type =\
            ctk.CTkOptionMenu(self.tabview.tab("2. Model head"),
                              values=["Regression",
                                      "Gaussian Mixture Model (GMM)"],
                              command=self.__get_model_head_name)
        
        self.model_head_type.grid(row=1, column=0, padx = 10, pady=5, sticky="w")        
        CTkToolTip(self.model_head_type, delay=0.1, bg_color = 'orange',
                   text_color = 'black', anchor='w',  wraplength=250, justify = 'left',
                   message='Output from the model class (e.g., LSTM or EA-LSTM) ' +
                   'is input to the model head. Here model head could be Regression or GMM. ' +
                   'Regression is multi Linear layers (see PyTorch for nn.Linear) with user ' +
                   'choice activation function.')
        
        # --------------------------------------Frame for regression model head
        self.regression_frame = ctk.CTkFrame(master=self.tabview.tab("2. Model head"), 
                                             fg_color = "transparent", border_width=0.0)
        self.regression_frame.grid_columnconfigure((0,1), weight=1)
        self.regression_frame.grid(row=2, column=0, sticky="w", pady=(5, 5))
                
        # Number of layers
        self.regression_nlayers_label = ctk.CTkLabel(self.regression_frame,
                                  text="2. Number of layers")
        self.regression_nlayers_label.grid(row=0, column=0, sticky="w", padx=10, pady=5)
        
        self.regression_nlayers = ctk.CTkOptionMenu(self.regression_frame,
                          values=list(map(str, range(1, 6))),
                          command=self.__create_entry_regression_model)
        self.regression_nlayers.grid(row=1, column=0, sticky="w", padx=10, pady=5)        
        CTkToolTip(self.regression_nlayers, delay=0.1, bg_color = 'orange',
                   text_color = 'black', anchor='w',  wraplength=250, 
                   message='Select number of linear layers. 1 should works for ' +
                   'most of the problems')
        
        # Label
        
        self.regression_config_label1 = ctk.CTkLabel(self.regression_frame,
                                  text="3. Number of neurons layer ith")
        self.regression_config_label1.grid(row=2, column=0, sticky="w", padx=10, pady=5) 
        CTkToolTip(self.regression_config_label1, delay=0.1, bg_color = 'orange',
                   text_color = 'black', anchor='w',  wraplength=250, justify = "left",
                   message='The last layer is the output layer. Therefore, the number of '+
                   'neurons for this layer is the number of target features, users '+
                   'DO NOT need to input the number of neurons for the last layer ' +
                   'If there is only 1 layer, this layer is also the last layer ') 
        
        self.regression_config_label2 = ctk.CTkLabel(self.regression_frame,
                                  text="4. Activation function layer ith")
        self.regression_config_label2.grid(row=2, column=1, sticky="w", padx=10, pady=5)

        self.option_menu = ctk.CTkOptionMenu(self.regression_frame,
                                             values=["Identity", "ReLu", "Sigmoid",
                                                     "Tanh", "Softplus"],
                                             command=self.__reg_get_acts_1)
        self.option_menu.grid(row=3, column=1, sticky="e", padx=10, pady=5)
        self.reg_activation_func = [self.option_menu]
                
        # --------------------------------------------------------Frame for GMM
        self.gmm_frame = ctk.CTkFrame(master=self.tabview.tab("2. Model head"), 
                                             fg_color = "transparent", border_width=0.0)
        self.gmm_frame.grid_columnconfigure((0,1), weight=1)
        #self.gmm_frame.grid(row=2, column=0, sticky="w", pady=(5, 5))
                
        # Number of neuron in hidden layer
        self.gmm_hidden_size_label = ctk.CTkLabel(self.gmm_frame,
                                  text="2. Work in progress (comming soon)...")
        self.gmm_hidden_size_label.grid(row=0, column=0, sticky="w", padx=10, pady=5)
        self.gmm_hidden_size = ctk.CTkEntry(master=self.gmm_frame,
                                            placeholder_text="None")
        self.gmm_hidden_size.grid(row=1, column=0, sticky="w", padx=10, pady=5)
                  
        # ---------------------------------------------Content of load data tab
        self.intro_label = ctk.CTkLabel(self.tabview.tab("1. Model class"), 
                                                   text="1. Select model class")
        self.intro_label.pack(anchor="w", pady = (10,10))
        
        self.model_class_type =\
            ctk.CTkOptionMenu(self.tabview.tab("1. Model class"),
                              values=["LSTM","EA-LSTM"], command=self.__get_model_class)
        CTkToolTip(self.model_class_type, delay=0.1, bg_color = 'orange', justify = "left",
                   text_color = 'black', anchor='w',  wraplength=250, 
                   message='The flow of data from input => output is as follows: ' + 
                   'Input => Model class => Model head => Ouput. ' +
                   'Model classes are: LSTM and EA-LSTM. Traditional LSTM, ' +
                   'dynamic and static inputs are concanated and feed into the LSTM. ' +
                   'while in EA-LSTM static input is feed into the input gate only. ' +
                   'See more in here https://doi.org/10.5194/hess-23-5089-2019')
                
        self.model_class_type.pack(anchor="w",  pady = 5)
                
        self.hidden_size_label = ctk.CTkLabel(self.tabview.tab("1. Model class"), 
                                                   text="2. Number of hidden units of the LSTM layer")
        self.hidden_size_label.pack(anchor="w", pady = (4,4))
        
        self.hidden_size = ctk.CTkEntry(master=self.tabview.tab("1. Model class"),
                                        placeholder_text="30")
        self.hidden_size.pack(anchor="w", pady = (4,4))
        CTkToolTip(self.hidden_size, delay=0.1, bg_color = 'orange', justify = "left",
                   text_color = 'black', anchor='w',  wraplength=250, 
                   message='Input number of hidden neurons of the LSTM (or EA-LSTM) ' +
                   '(most problems should work with any values between 20 to 516). ' +
                   self.ray_tooltip)
        
        self.hidden_size.bind('<KeyRelease>', self.__get_hidden_size)

        self.nlayers_label = ctk.CTkLabel(self.tabview.tab("1. Model class"), 
                                               text="3. Number of LSTM layers")
        self.nlayers_label.pack(anchor="w", pady = (4,4))
        self.nlayers= ctk.CTkOptionMenu(self.tabview.tab("1. Model class"),
                                             values=list(map(str,list(range(1,6,1)))),
                                             command=self.__get_num_layers) 
        self.nlayers.pack(anchor="w", pady = (4,4))
        CTkToolTip(self.nlayers, delay=0.1, bg_color = 'orange', justify = "left",
                   text_color = 'black', anchor='w',  wraplength=250, 
                   message='The number of layers of the LSTM (or EA-LSTM).' +
                   ' 1 should work for most of the problems')
        
        self.dropout_label = ctk.CTkLabel(self.tabview.tab("1. Model class"), 
                                               text="4. Dropout rate")
        self.dropout_label.pack(anchor="w", pady = (4,4))
        self.dropout = ctk.CTkEntry(master=self.tabview.tab("1. Model class"),
                                        placeholder_text="0.30")
        self.dropout.pack(anchor="w", pady = (4,4))
        self.dropout.bind('<KeyRelease>', self.__get_dropout)
        CTkToolTip(self.dropout, delay=0.1, bg_color = 'orange', justify = "left",
                   text_color = 'black', anchor='w',  wraplength=250, 
                   message='This value is only used if the number of layers > 1.' +
                   'During training, randomly zeroes some of the elements of the ' +
                   'input tensor to the i_th layer with probability p using samples ' +
                   'from a Bernoulli distribution. Commons values are from 0.2 to 0.5')

        
    # -------------------------------------------------content of load data tab
    def __show_model_head_class(self):
        
        # Get link to the image
        image = Path(__file__).parents[1]
        button_image = ctk.CTkImage(Image.open( 
            Path(image, "images/model_head_class.png")),
            size=(500, 500))
        
        # Create new window 
        self.new_window = ctk.CTkToplevel(self, fg_color = "white")
        ctk.CTkLabel(master=self.new_window, image=button_image, text = "").pack()
            
    def __get_hidden_size(self, dummy):
        # Get number of hidden layers
        get_input_text = self.hidden_size.get().strip()
        
        try:
            self.config["hidden_size"] = int(float(get_input_text))
            print("hidden size = ", self.config["hidden_size"])
            self.hidden_size.configure(fg_color = '#d3ffc7')
            self.error_label.configure(text=" ")
        except:
            try:
                eval(get_input_text)
                self.config["hidden_size"] = get_input_text
                print("hidden size = ", self.config["hidden_size"])
                self.hidden_size.configure(fg_color = '#d3ffc7')
                self.error_label.configure(text=" ")
            except:
                self.hidden_size.configure(fg_color = '#ffc7c7')
                self.error_label.configure(text=self.__message_text_tune("integer"), 
                                           text_color = "red")
            
    # Get number of lstm layers
    def __get_num_layers(self, nlayer: str):
        try:
            self.config["num_layers"] = int(nlayer)
            print("num_layers = ", self.config["num_layers"])
        except:
            pass
        
    # Message box for error in input with tune search space 
    def __message_text_tune(self, data_type):
        out_message=("Input should be " + data_type + " or Tune Search Space API command: " +
            "https://docs.ray.io/en/latest/tune/api/search_space.html")
        return out_message

            
    # Get number of lstm layers
    def __get_dropout(self, dummy: str):
        
        get_input_text = self.dropout.get().strip()
        
        try:
            self.config["dropout"] = float(get_input_text)
            print("drop out rate = ", self.config["dropout"])
            self.dropout.configure(fg_color = '#d3ffc7')
        except:
            try:
                eval(get_input_text)
                self.config["dropout"] = get_input_text
                print("drop out rate = ", self.config["dropout"])
                self.dropout.configure(fg_color = '#d3ffc7')
            except:
                self.dropout.configure(fg_color = '#ffc7c7')

    def __get_model_head_name(self, model_head_name: str):
        model_head_names = {"Regression" : "Regression",
                            "Gaussian Mixture Model (GMM)": "GMM"}
        
        self.globalData["model_head"] = model_head_names[model_head_name]
        print("Model head name = ", self.globalData["model_head"])
            
        # Delete config if other model head option is 
        if self.globalData["model_head"] == "Regression":
                       
            self.regression_frame.grid(row=2, column=0, sticky="w", pady=(5, 5))
            self.gmm_frame.grid_forget()
            
            self.config["Regression"] = {}
        else:
            # Hide regression frame
            self.regression_frame.grid_forget()
            self.gmm_frame.grid(row=2, column=0, sticky="w", pady=(5, 5))
            try:
                del self.config["Regression"]
            except:
                pass
 
    def __get_model_class(self, model_class: str):
        self.config["model_class"] = model_class
        print("Model class name = ", self.config["model_class"])
        
        if model_class == "EA-LSTM":
            tk.messagebox.showinfo(title="Message box", 
                                   message="This model class takes a lot of time to train " +
                                   "need to improve the forward pass for this model class")         
            
    def __create_entry_regression_model(self, nlayers: str):
        print("number of layer", int(nlayers))
        
        # try to hide all entry
        try:
            for entry in self.reg_neurons:
                entry.grid_forget()
        except:
            pass
        
        # try to hide all entry
        try:
            for entry in self.reg_activation_func:
                entry.grid_forget()
        except:
            pass
        
        # Now add entry according to the number of layers
        if "Regression" in self.config.keys():
            
            row_number = 3
            self.config["Regression"]["num_layers"] = int(nlayers)
            self.reg_neurons = []
            self.reg_activation_func = []
            self.config["Regression"]["num_neurons"] = [None for i in range(int(nlayers))]
            self.config["Regression"]["activation_function"] = ["Identity" for i in 
                                                         range(int(nlayers))]

            get_neurons = {0: self.__reg_get_neurons_1, 1: self.__reg_get_neurons_2,
                           2: self.__reg_get_neurons_3, 3: self.__reg_get_neurons_4}
            get_acts = {0: self.__reg_get_acts_1, 1: self.__reg_get_acts_2,
                        2: self.__reg_get_acts_3, 3: self.__reg_get_acts_4,
                        4: self.__reg_get_acts_5}
            
            for i in range(int(nlayers)):

                if i < int(nlayers) - 1:
                    entry = ctk.CTkEntry(master=self.regression_frame,
                                         placeholder_text="10")
                    entry.grid(row=row_number, column=0, sticky="e", padx=10, pady=5)
                    self.reg_neurons.append(entry)
                    self.reg_neurons[i].bind('<KeyRelease>', get_neurons[i])
                
                option_menu = ctk.CTkOptionMenu(self.regression_frame,
                                                     values=["Identity", "ReLu", "Sigmoid",
                                                             "Tanh", "Softplus"],
                                                     command=get_acts[i])
                option_menu.grid(row=row_number, column=1, sticky="e", padx=10, pady=5)
                self.reg_activation_func.append(option_menu)
                row_number += 1
                
                try:
                    CTkToolTip(self.reg_neurons[i], delay=0.1, bg_color = 'orange',
                               text_color = 'black', anchor='w',  wraplength=250, justify = "left",
                               message='Input the number of neurons of the ' + 
                               str(i + 1) + ' layer (please give an integer number)')
                except:
                    pass
                
    # Function get number of neuron in each output layer
    def __get_num_neuron(self, layer):    
        try:
            get_input_text = self.reg_neurons[layer].get().strip()
            self.config["Regression"]["num_neurons"][layer] = int(float(get_input_text))
            print("Num of neurons layer " + str(layer + 1) + " = ", 
                  self.config["Regression"]["num_neurons"][layer])
            self.reg_neurons[layer].configure(fg_color = '#d3ffc7')
        except:
            self.reg_neurons[layer].configure(fg_color = '#ffc7c7')


    # Functions to get number of input neurons each layer - Make this code clearner
    def __reg_get_neurons_1(self, dummy):
        self.__get_num_neuron(0)

    def __reg_get_neurons_2(self, dummy):
        self.__get_num_neuron(1)

    def __reg_get_neurons_3(self, dummy):
        self.__get_num_neuron(2)
        
    def __reg_get_neurons_4(self, dummy):
        self.__get_num_neuron(3)
    
    # Function to get activation function of each layer - Make this code clearner
    def __reg_get_acts_1(self, dummy):
        self.config["Regression"]["activation_function"][0] = dummy
        print("Activation function of layer 1 = ", dummy)
    def __reg_get_acts_2(self, dummy):
        self.config["Regression"]["activation_function"][1] = dummy
        print("Activation function of layer 2 = ", dummy)
    def __reg_get_acts_3(self, dummy):
        self.config["Regression"]["activation_function"][2] = dummy
        print("Activation function of layer 3 = ", dummy)
    def __reg_get_acts_4(self, dummy):
        self.config["Regression"]["activation_function"][3] = dummy
        print("Activation function of layer 4 = ", dummy)
    def __reg_get_acts_5(self, dummy):
        self.config["Regression"]["activation_function"][5] = dummy
        print("Activation function of layer 5 = ", dummy)
