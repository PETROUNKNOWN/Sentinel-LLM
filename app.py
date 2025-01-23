import ollama
import customtkinter as ctk


# Initialize the OLLA client


class ChatApp:
    def __init__(self, root):
        self.root=root
        self.root.title("Sentinel cb_llama3.2:3B")
        self.root.geometry("1000x500,+800+250")
        # self.root.resizable(0,0)
        self.root.columnconfigure(1,weight=1)
        self.root.rowconfigure(0,weight=1)
        # self.root.rowconfigure(1,weight=1)
        self.rowCounter=1
        self.buttonAvailabilityFlag=True

        sidebarframe=ctk.CTkFrame(root,fg_color="#101010",border_color="#ff0000",border_width=1,width=200)
        sidebarframe.grid(row=0,column=0,rowspan=2,sticky="nsew",padx=2,pady=0)
        self.chatframe=ctk.CTkScrollableFrame(root,fg_color="#101010",border_color="#ff0000",border_width=1)
        self.chatframe.grid(row=0,column=1,sticky="nsew",padx=2,pady=2)
        self.chatframe.columnconfigure(0,weight=1)
        self.chatframe.rowconfigure(0,weight=1)
        messageframe=ctk.CTkFrame(root,fg_color="#101010",border_color="cyan",border_width=1,height=50)
        messageframe.grid(row=1,column=1,sticky="nsew",padx=2,pady=2)
        messageframe.columnconfigure(0,weight=1)
        messageframe.rowconfigure(0,weight=1)
        self.constructor_chatContainer("MODEL","Hello there. \nHow can be of assistance today?").grid(row=self.rowCounter,column=0,sticky="nsew",padx=2,pady=2)
        # self.constructor_chatContainer("USER","").grid(row=self.rowCounter,column=0,sticky="nsew",padx=2,pady=2)
        # self.constructor_chatContainer("SYSTEM","SYSTEM ERROR! PLEASE TRY AGAIN.").grid(row=self.rowCounter,column=0,sticky="nsew",padx=2,pady=2)

        textEntry=ctk.CTkEntry(messageframe,border_color="#ff0000",border_width=1)
        textEntry.grid(row=0,column=0,sticky="nsew",padx=2,pady=2)
        self.sendButton=ctk.CTkButton(messageframe,text="Send",border_color="#ff0000",border_width=1,command=lambda: self.getInput(str(textEntry.get())))
        self.sendButton.grid(row=0,column=1,sticky="nsew",padx=2,pady=2)


    def constructor_chatContainer(self,caller,myText):
        self.rowCounter+=1
        chatContainer=ctk.CTkFrame(self.chatframe,fg_color="#101010",border_color="blue",border_width=0,height=20)
        chatContainer.columnconfigure(1,weight=1)
        chatCard=ctk.CTkFrame(chatContainer,fg_color="#101010",border_color="green",border_width=1,width=200)
        if caller=="MODEL":
            stickyPlace="nsw"
        elif caller=="USER":
            stickyPlace="nse"
        elif caller=="SYSTEM":
            stickyPlace="ew"
        else:
            print("Error: Caller not specified.")
            stickyPlace="nsew"


        
        
        chatCard.grid(row=1,column=1,sticky=stickyPlace,padx=2,pady=2)
        chatCard.columnconfigure(0,weight=1)
        chatCard.rowconfigure(0,weight=1)
        
        thisText=ctk.CTkLabel(chatCard,text=myText,wraplength=300,justify="left")
        thisText.grid(row=0,column=0,sticky="nsew",padx=2,pady=2,ipadx=8,ipady=8)
        return chatContainer

    def getInput(self,message):
        # self.buttonAvailabilityFlag=False
        # self.sendButton.configure(state="disabled")
        self.constructor_chatContainer("USER",message).grid(row=self.rowCounter,column=0,sticky="nsew",padx=2,pady=2)
        self.getResponse(message)

    def getResponse(self,message):
        client = ollama.Client()

        # Set up the model and prompt
        model = "Sentinel"
        # prompt = "What is your name?"

        # Generate an initial response from the model
        response = client.generate(model=model, prompt=message)
        # print(f"Response from model: {model}")
        # print(response.response)
        thisResponse=str(response.response)
        while thisResponse==False:
            self.sendButton.configure(state="disabled")
        self.sendButton.configure(state="normal")
        self.constructor_chatContainer("MODEL",thisResponse).grid(row=self.rowCounter,column=0,sticky="nsew",padx=2,pady=2)


if __name__ == "__main__":
    ctk.set_appearance_mode("System")
    app_root=ctk.CTk()
    app=ChatApp(app_root)
    app_root.mainloop()