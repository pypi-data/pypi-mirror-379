

def write_multicell_with_styles(self, max_width, cell_height, text_list):

        # Source:https://stackoverflow.com/questions/60736940/how-to-make-inline-bold-text-using-pyfpdf#
        startx = self.get_x()
        self.set_font('Arial', '', 12)

        #loop through differenct sections in different styles
        for text_part in text_list:
            #check and set style
            try:
                current_style = text_part['style']
                self.set_font('Arial', current_style, 12)
            except KeyError:
                self.set_font('Arial', '', 12)

            #loop through words and write them down
            space_width = self.get_string_width(' ')
            for word in text_part['text'].split(' '):
                current_pos = self.get_x()
                word_width = self.get_string_width(word)
                #check for newline
                if (current_pos + word_width) > (startx + max_width):
                    #return 
                    self.set_y(self.get_y() + cell_height)
                    self.set_x(startx)
                self.cell(word_width, 5, word)
                #add a space
                self.set_x(self.get_x() + space_width)