# generate_html.py
# Generates html for Alif Baa media files.

import os
from natsort import natsorted

units = natsorted([unit for unit in os.listdir('.') if 'Unit' in unit and 'html' not in unit])

def generate_index():
    def unit_header(unit):
        unit_name = unit.replace('_', ' ')
        unit_link_html = unit+'.html'
        unit_header_html = """
            <h2><a href='%s'>%s</a></h2>
        """ % (unit_link_html, unit_name)
        
        return unit_header_html

    html_string = """
    <!doctype html> 
    <html lang='en'> 
    <head>
        <title>Alif Baa 3rd Edition</title>
        <meta name='robots' content='noindex, nofollow'>
        <style>body {font-family: Sans-Serif}</style>
    </head>
    <body>
        <h1>Alif Baa 3rd Edition</h1>
    """

    for unit in units:
        html_string += unit_header(unit)

    html_string += """
    </body>
    </html>
    """

    return html_string

def generate_unit_page(unit):

    def section_exercises(section):
        section_name = section.replace('_', ' ')
        section_html =  """
            <h2>%s</h2>
        """ % (section_name)

        exercises = natsorted(os.listdir(unit+'/'+section))

        for exercise in exercises:
            exercise_name = exercise.split('.')[0].replace('_', ' ')
            exercise_html = """
                <h3>%s</h3>
            """ % (exercise_name)

            media_url = unit+'/'+section+'/'+exercise

            if 'mp4' in exercise:
                exercise_html += """
                    <video width='640' height='480' controls='controls'>
                        <source src='%s' type='video/mp4' />
                    </video>
                """ % (media_url)
            elif 'mp3' in exercise:
                exercise_html += """
                    <audio controls='controls'>
                        <source src='%s'type="audio/mp3" />
                    </audio>
                """ % (media_url)

            section_html += exercise_html

        return section_html

    unit_name = unit.replace('_', ' ')
    sections = natsorted(os.listdir(unit))

    html_string = """
    <!doctype html> 
    <html lang='en'> 
    <head>
        <title>Alif Baa %s</title>
        <meta name='robots' content='noindex, nofollow'>
        <style>body {font-family: Sans-Serif}</style>
    </head>
    <body>
        <h1>%s</h1>
    """ % (unit_name, unit_name)

    for section in sections:
        html_string += section_exercises(section)

    html_string += """
    </body>
    </html>
    """

    return html_string

def write_index():
    with open('index.html', 'w') as html_file:
        html_file.write(generate_index())

def write_units():
    for unit in units:
        with open(unit+'.html', 'w') as unit_html_file:
            unit_html_file.write(generate_unit_page(unit))

if __name__ == '__main__':
    write_index()
    write_units()
