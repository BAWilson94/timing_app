import streamlit as st
import datetime
import time

import math



#define a couple of useful functions
def stylable_container(key: str, css_styles: str | list[str]) -> "DeltaGenerator":
    """
    Insert a container into your app which you can style using CSS.
    This is useful to style specific elements in your app.

    Args:
        key (str): The key associated with this container. This needs to be unique since all styles will be
            applied to the container with this key.
        css_styles (str | List[str]): The CSS styles to apply to the container elements.
            This can be a single CSS block or a list of CSS blocks.

    Returns:
        DeltaGenerator: A container object. Elements can be added to this container using either the 'with'
            notation or by calling methods directly on the returned object.
    """
    if isinstance(css_styles, str):
        css_styles = [css_styles]

    # Remove unneeded spacing that is added by the style markdown:
    css_styles.append(
        """
> div:first-child {
    margin-bottom: -1rem;
}
"""
    )

    style_text = """
<style>
"""

    for style in css_styles:
        style_text += f"""

div[data-testid="stVerticalBlock"]:has(> div.element-container > div.stMarkdown > div[data-testid="stMarkdownContainer"] > p > span.{key}) {style}

"""

    style_text += f"""
    </style>

<span class="{key}"></span>
"""

    container = st.container()
    container.markdown(style_text, unsafe_allow_html=True)
    return container

def time_dif(event):
    """Create a way to extract the days, hours, minutes and seconds
    
    Args:
        event (datetime): datetime object for the event in question
    Returns:
        times (list): list of times as, days, hours, minutes and seconds
    """
    event_delta = event-datetime.datetime.now()
    if event_delta > datetime.timedelta(0):
        days = event_delta.days
        hours = math.floor(event_delta.seconds/3600)
        minutes = math.floor(event_delta.seconds/60) - (hours * 60)
        seconds = event_delta.seconds - (hours * 3600) - (minutes * 60)
    else:
        days,hours,minutes,seconds = 0,0,0,0
    return days,hours,minutes,seconds
    


#Set up the background image
import base64

#@st.cache(allow_output_mutation=True)
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_png_as_page_bg(png_file):
    bin_str = get_base64_of_bin_file(png_file)
    page_bg_img = '''
    <style>
    stApp {
    background-image: url("data:image/png;base64,%s");
    background-size: cover;
    }
    </style>
    ''' % bin_str
    
    st.markdown(page_bg_img, unsafe_allow_html=True)
    return

set_png_as_page_bg('Sydney-Harbour-Bridge.png')

#page_bg_img = '''
#<style>
#body {
#background-image: url("https://s1.at.atcdn.net/wp-content/uploads/2005/09/Sydney-Harbour-Bridge.jpg");
#background-size: cover;
#}
#</style>
#'''
#
#st.markdown(page_bg_img, unsafe_allow_html=True)

st.markdown("""
    <style>
        .block-container {padding-top: 0 !important;}
    </style>
    """,
    unsafe_allow_html=True,
)

    
#if __name__ == "__main__":
Leave_work = datetime.datetime(2025,2,7,17,00,00)
Flight_time = datetime.datetime(2025,2,9,21,00,00)
Landing_time = datetime.datetime(2025,2,10,23,00,00)
Start_work = datetime.datetime(2025,2,16,22,00,00)


#    st.title("Ben's Timeline")

st.write("##")

#Construct the leave work timer
temp_days, temp_hours, temp_mins, temp_seconds = time_dif(Leave_work)
with st.container(key="leave_work"):
    left_col1,right_col1 = st.columns([61,39])
    with left_col1:
            st.title("Last day at Method:")
    with right_col1:
        with stylable_container(
                key="leave_work_right",
                css_styles="""
                    {
                        background-color: black;
                        color: red;
                        border-radius: 0px;
                        padding-left: 10px;
                    }
                    """,
        ):
            if temp_days < 10:
                str_days = "0"+str(temp_days)
            else:
                str_days = str(temp_days)
            if temp_hours < 10:
                str_hours = "0"+str(temp_hours)
            else:
                str_hours = str(temp_hours)
            if temp_mins < 10:
                str_mins = "0"+str(temp_mins)
            else:
                str_mins = str(temp_mins)
            if temp_seconds < 10:
                str_seconds = "0"+str(temp_seconds)
            else:
                str_seconds = str(temp_seconds)
            
        
            st.title("-"+str_days+':'+str_hours+':'+str_mins+':'+str_seconds)
            st.html("<p> &emsp; Days &emsp;&ensp; Hrs &emsp;&ensp; Mins &emsp;&ensp; Secs</p>")


#st.write("######")
with st.container(key="flight_time"):
    #Construct the flight timer
    temp_days, temp_hours, temp_mins, temp_seconds = time_dif(Flight_time)
    
    left_col2,right_col2 = st.columns([61,39])
    with left_col2:
        st.title("Take-off Heathrow:")
    with right_col2:
        with stylable_container(
                key="take_off_right",
                css_styles="""
                    {
                        background-color: black;
                        color: red;
                        padding-left: 10px;
                        line-height:- 10px;
                    }
                    """,
        ):
            if temp_days < 10:
                str_days = "0"+str(temp_days)
            else:
                str_days = str(temp_days)
            if temp_hours < 10:
                str_hours = "0"+str(temp_hours)
            else:
                str_hours = str(temp_hours)
            if temp_mins < 10:
                str_mins = "0"+str(temp_mins)
            else:
                str_mins = str(temp_mins)
            if temp_seconds < 10:
                str_seconds = "0"+str(temp_seconds)
            else:
                str_seconds = str(temp_seconds)
            
        
            st.title("-"+str_days+':'+str_hours+':'+str_mins+':'+str_seconds)
            st.html("<p> &emsp; Days &emsp;&ensp; Hrs &emsp;&ensp; Mins &emsp;&ensp; Secs</p>")



#st.write("######")
#Construct the landing time timer
temp_days, temp_hours, temp_mins, temp_seconds = time_dif(Landing_time)
with st.container(key="landing_time"):
    left_col1,right_col1 = st.columns([61,39])
    with left_col1:
        st.title("Landing at Sydney:")
    with right_col1:
        with stylable_container(
                key="landing_time_right",
                css_styles="""
                    {
                        background-color: black;
                        color: red;
                        border-radius: 0px;
                        padding-left: 10px;
                    }
                    """,
        ):
            if temp_days < 10:
                str_days = "0"+str(temp_days)
            else:
                str_days = str(temp_days)
            if temp_hours < 10:
                str_hours = "0"+str(temp_hours)
            else:
                str_hours = str(temp_hours)
            if temp_mins < 10:
                str_mins = "0"+str(temp_mins)
            else:
                str_mins = str(temp_mins)
            if temp_seconds < 10:
                str_seconds = "0"+str(temp_seconds)
            else:
                str_seconds = str(temp_seconds)
            
        
            st.title("-"+str_days+':'+str_hours+':'+str_mins+':'+str_seconds)
            st.html("<p> &emsp; Days &emsp;&ensp; Hrs &emsp;&ensp; Mins &emsp;&ensp; Secs</p>")
                

with st.container(key="Staring_work"):
    #Construct the flight timer
    temp_days, temp_hours, temp_mins, temp_seconds = time_dif(Start_work)
    
    left_col2,right_col2 = st.columns([61,39])
    with left_col2:
        st.title("First day at T&T:")
    with right_col2:
        with stylable_container(
                key="start_work_right",
                css_styles="""
                    {
                        background-color: black;
                        color: red;
                        padding-left: 10px;
                        line-height:- 10px;
                    }
                    """,
        ):
            if temp_days < 10:
                str_days = "0"+str(temp_days)
            else:
                str_days = str(temp_days)
            if temp_hours < 10:
                str_hours = "0"+str(temp_hours)
            else:
                str_hours = str(temp_hours)
            if temp_mins < 10:
                str_mins = "0"+str(temp_mins)
            else:
                str_mins = str(temp_mins)
            if temp_seconds < 10:
                str_seconds = "0"+str(temp_seconds)
            else:
                str_seconds = str(temp_seconds)
            
        
            st.title("-"+str_days+':'+str_hours+':'+str_mins+':'+str_seconds)
            st.html("<p> &emsp; Days &emsp;&ensp; Hrs &emsp;&ensp; Mins &emsp;&ensp; Secs</p>")

#if st.button('stop'):
#    time.sleep(1000)
time.sleep(1)
st.rerun()
