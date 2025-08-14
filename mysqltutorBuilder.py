
mysqltutor_helper = """
MDFloatLayout:
    BoxLayout:
        orientation: "vertical"
        size: root.width, root.height

        Label:
            id: word_label
            text_size: self.size
            halign: "center"
            valign: "middle"
            text: "Enter a Name"
            font_size: 32
            
        TextInput:
            id: word_input
            multiline: False
            size_hint: (1, .5)
        
        Button:
            size_hint: (1, .5)
            font_size: 32
            text: "Submin a Name"
            on_press: app.submit()
        
        Button:
            size_hint: (1, .5)
            font_size: 32
            text: "Show Record"
            on_press: app.show_record()

"""