import streamlit as st
import streamlit.components.v1 as components
from PIL import Image
import os
import matplotlib.pyplot as plt
from streamlit_d3graph import d3graph
import base64

# Using object notation




st.header("**IPL AUCTION 2022**")
st.text("")
st.text("")
st.write("The 2022 Indian Premier League, also known as IPL 15 or for sponsorship reasons, TATA IPL 2022, was the fifteenth season of the Indian Premier League (IPL), a professional Twenty20 cricket league established by the Board of Control for Cricket in India (BCCI) in 2007. The tournament was played from 26 March 2022 to 29 May 2022. The group stage of the tournament was played entirely in the state of Maharashtra, with Mumbai, Navi Mumbai and Pune hosting matches.")
st.write("The IPL auction is an annual event where teams participating in the Indian Premier League (IPL) bid for players to add to their squad for the upcoming season. The auction for the 2022 IPL was held on February 12, 2022, in Bengaluru, India. A total of 292 players were included in the auction, out of which 123 were bought by the eight participating teams.")
st.write("The season saw the expansion of the league with the addition of two new franchises.Lucknow SuperGiants and Gujrat Titans")
st.write("Each existing team was allowed to retain a maximum of four players, with the two new teams were allowed to select a maximum of three players before the auction.")
st.text("")
st.text("") 
st.text("")
st.text("")
st.text("")

st.image("https://english.cdn.zeenews.com/sites/default/files/styles/zm_700x400/public/2022/02/01/1010809-ipl-2022-auction.jpg")
st.text("")

st.write("The two-day long IPL auction in Bengaluru saw 204 players being sold to 10 franchises for a total of Rs 551.70 crore. Current India internationals were the hot-favourites for obvious reasons but big overseas names like David Warner, Jofra Archer, Pat Cummins, Trent Boult, Liam Livingstone earned the big bucks too. India wicketkeeper-batter Ishan Kishan was the most expensive buy of IPL 2022 auction. The left-hander was picked up by Mumbai Indians for Rs 15.25 crore. All-rounder Deepak Chahar was bought by Chennai Super Kings (CSK) for Rs 14 crore. Kolkata Knight Riders, who needed a captain, went all out to bag Shreyas Iyer for Rs 12.25 crore. The most expensive among overseas cricketers was England’s Liam Livingstone, who went for Rs 11.5 crore to Punjab Kings. Harshal Patel (Rs 10.75 crore to RCB), Shardul Thakur (Rs 10.75 crore to DC) were the other big picks. Avesh Khan, who was picked up by Lucknow Super Giants for Rs 10 crore, became the most expensive uncapped player in the history of IPL auction.")
st.write("While CSK and MI were not very active on Day 1 of the IPL 2022 mega auction, they spent more than Rs 10 crore on a player for the first time in the history of the auction. Chennai paid Rs 14 crore to buy back all-rounder Deepak Chahar.")

st.title("Tableau Project")

components.html(
        """
        <div class='tableauPlaceholder' id='viz1678396335764' style='position: relative'><noscript><a href='#'><img
                alt='Dashboard 2 '
                src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;IP&#47;IPL_2022_Auction_16783962728710&#47;Dashboard2&#47;1_rss.png'
                style='border: none' /></a></noscript><object class='tableauViz' style='display:none;'>
                <param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' />
                <param name='embed_code_version' value='3' />
                <param name='site_root' value='' />
                <param name='name' value='IPL_2022_Auction_16783962728710&#47;Dashboard2' />
                <param name='tabs' value='no' />
                <param name='toolbar' value='yes' />
                <param name='static_image'
                    value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;IP&#47;IPL_2022_Auction_16783962728710&#47;Dashboard2&#47;1.png' />
                <param name='animate_transition' value='yes' />
                
                <param name='display_static_image' value='yes' />
                <param name='display_spinner' value='yes' />
                <param name='display_overlay' value='yes' />
                <param name='display_count' value='yes' />
                <param name='language' value='en-US' />
                <param name='filter' value='publish=yes' />
            </object></div>
        
        <script type='text/javascript'> 
            var divElement = document.getElementById('viz1678396335764'); 
            var vizElement = divElement.getElementsByTagName('object')[0]; 
            if (divElement.offsetWidth > 800) { 
                vizElement.style.width = '1900px'; 
                vizElement.style.height = '1062px'; 
            } 
            else if (divElement.offsetWidth > 500) { 
                vizElement.style.width = '1900px'; 
                vizElement.style.height = '1062px'; 
            } 
            else { 
                vizElement.style.width = '100%'; 
                vizElement.style.height = '100%'; 
            } 
            var scriptElement = document.createElement('script'); 
            scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js'; 
            vizElement.parentNode.insertBefore(scriptElement, vizElement);                
        </script> """, height=1000, width=2000)
st.write("Kane Williamson will be the first option for SRH in their IPL 2022 players retention. If SRH decides to build a strong bowling unit with Indian players then Natarajan and Bhuvneshwar Kumar will be the better options, which they brought back in the Auction.")
st.write("Royal Challengers Banglore retained Virat Kohli in their first retained player slot for Rs. 15 crores, followed by Australian all-rounder Glenn Maxwell for Rs. 11 crores and their last retention is Siraj where he bagged Rs. 7 crores.")
st.write("Punjab Kings needs to utilize this mega auction opportunity to build a strong team that could lift their maiden IPL trophy in the upcoming season.PBKS retained just 2 players out of 4 players’ options. Mayank Agarwal and Arshdeep Singh were retained by the PBKS ahead of PL 2022 Mega Auction.")
st.write(" Chennai Super Kings looks its all possible way to retain Ruturaj Gaikwad who plays a crucial role in winning IPL 2021 trophy. Notably, Ruturaj Gaikwad is the orange cap holder of IPL 2021.")
st.write("Delhi Capitals all set to retain Rishabh Pant, Prithvi Shaw, Axar Patel, and Anrich Nortje. Thinking of building a young team DC had to skip their opening batter Dhawan")
st.write(" Venkatesh Iyer made his IPL debut in the IPL 2021 and scored 370 runs with 3 wickets while playing 10 matches of the season. KKR will also not dare to lose Varun Chakaravarthy who plays a vital role in KKR’s success in the past 2 seasons.Kolkata Knight Riders retained their two all-rounders Sunil Narine and Andre Russell while they want to keep Varun Chakravarty, Venkatesh Iyer as Indian core.")
st.write("Rajasthan Royals needs to utilize this mega auction opportunity to build a strong team that could lift their second IPL trophy in the upcoming season.Sanju Samson will continue to captain the side, Jos Buttler is retained alongside young indian opener Yashasvi Jaiswal.")
st.write("The Gujarat Titans bags Rashid Khan and Hardik Pandya for Rs 15 crores each while the franchise bags Shubman Gill for Rs 8 Crores INR.It is also learned that Hardik Pandya named as captain of the Gujarat Titans")
st.write("Lucknow Super Giants ropes KL Rahul for INR 17 crores followed by Marcus Stoinis for INR 9.2 crores and uncapped Ravi Bishnoi for INR 4 crores.")

st.image("https://images.indianexpress.com/2022/02/WhatsApp-Image-2022-02-11-at-4.49.10-PM.jpeg")

st.title("Python")
st.write("**It shows the percentage of bowler,batesman,all rounder,wicketkeeper in a team**")
option = st.selectbox("TypeS of Players Bought by Teams in IPL 2022",
                          ("CSK", "DC", "GT", "KKR", "MI", "PK", "SH", "RCB", "RR"))

if option == "CSK":
        labels = 'All Rounder', 'Bowler', 'Batsman', 'WicketKeeper'
        sizes = [36, 32, 20, 12]
        explode = (0.1, 0, 0, 0)

        fig1, ax1 = plt.subplots()
        ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
                shadow=True, startangle=90)
        # Equal aspect ratio ensures that pie is drawn as a circle.
        ax1.axis('equal')
        st.pyplot(fig1)

if option == "DC":
        labels = 'All Rounder', 'Bowler', 'Batsman', 'WicketKeeper'
        sizes = [37.5, 29.2, 20.8, 12.5]
        explode = (0.1, 0, 0, 0)

        fig1, ax1 = plt.subplots()
        ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
                shadow=True, startangle=90)
        # Equal aspect ratio ensures that pie is drawn as a circle.
        ax1.axis('equal')
        st.pyplot(fig1)

if option == "GT":
        labels = 'All Rounder', 'Bowler', 'Batsman', 'WicketKeeper'
        sizes = [36.4, 36.4, 18.2, 9.09]
        explode = (0.1, 0.1, 0, 0)

        fig1, ax1 = plt.subplots()
        ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
                shadow=True, startangle=90)
        # Equal aspect ratio ensures that pie is drawn as a circle.
        ax1.axis('equal')
        st.pyplot(fig1)

if option == "RR":
        labels = 'All Rounder', 'Bowler', 'Batsman', 'WicketKeeper'
        sizes = [25, 41.7, 20.8, 12.5]
        explode = (0, 0.1, 0, 0)

        fig1, ax1 = plt.subplots()
        ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
                shadow=True, startangle=90)
        # Equal aspect ratio ensures that pie is drawn as a circle.
        ax1.axis('equal')
        st.pyplot(fig1)

if option == "RCB":
        labels = 'All Rounder', 'Bowler', 'Batsman', 'WicketKeeper'
        sizes = [40.9, 31.8, 13.6, 13.6]
        explode = (0.1, 0, 0, 0)

        fig1, ax1 = plt.subplots()
        ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
                shadow=True, startangle=90)
        # Equal aspect ratio ensures that pie is drawn as a circle.
        ax1.axis('equal')
        st.pyplot(fig1)

if option == "SH":
        labels = 'All Rounder', 'Bowler', 'Batsman', 'WicketKeeper'
        sizes = [26.1, 39.1, 21.7, 13]
        explode = (0, 0.1, 0, 0)

        fig1, ax1 = plt.subplots()
        ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
                shadow=True, startangle=90)
        # Equal aspect ratio ensures that pie is drawn as a circle.
        ax1.axis('equal')
        st.pyplot(fig1)

if option == "PK":
        labels = 'All Rounder', 'Bowler', 'Batsman', 'WicketKeeper'
        sizes = [44, 32, 12, 12]
        explode = (0.1, 0, 0, 0)

        fig1, ax1 = plt.subplots()
        ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
                shadow=True, startangle=90)
        # Equal aspect ratio ensures that pie is drawn as a circle.
        ax1.axis('equal')
        st.pyplot(fig1)

if option == "MI":
        labels = 'All Rounder', 'Bowler', 'Batsman', 'WicketKeeper'
        sizes = [44, 28, 20, 6]
        explode = (0.1, 0, 0, 0)

        fig1, ax1 = plt.subplots()
        ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
                shadow=True, startangle=90)
        # Equal aspect ratio ensures that pie is drawn as a circle.
        ax1.axis('equal')
        st.pyplot(fig1)

if option == "KKR":
        labels = 'All Rounder', 'Bowler', 'Batsman', 'WicketKeeper'
        sizes = [40, 28, 20, 12]
        explode = (0.1, 0, 0, 0)

        fig1, ax1 = plt.subplots()
        ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
                shadow=True, startangle=90)
        # Equal aspect ratio ensures that pie is drawn as a circle.
        ax1.axis('equal')
        st.pyplot(fig1)


st.title("D3.js Project")
st.write("**It shows the funds spent in crores on the y axis versus the team names on the x-axis**")
components.html(
        """
            
    <!DOCTYPE html>
    <html>
    <head>
    <title>D3.js Tutorial</title>
    <script src="https://d3js.org/d3.v5.min.js"></script>
    <style>
        body {
        font-family: Arial, Helvetica, sans-serif;
        color:white;
        }

        .rect:hover { opacity: 0.5; }
    </style>
    </head>
    <body>
    <div style="text-align: center;">
        <div id="d3-container" />
    </div>
    <script type="text/javascript">
        const data = [
    { name: 'DC', score: 50 },
    { name: 'RR', score: 45 },
    { name: 'RCB', score: 51 },
    { name: 'SRH', score: '21'},
    { name: 'MI', score: 70 },
    { name: 'GT', score: 35 },
    { name: 'CSK', score: 48 },
    { name: 'LSG', score: 29 },
    { name: 'KKR', score: 39 },
    { name: 'PBKS', score: 46 },
    
    ];

    const width = 800;
    const height = 600;
    const margin = { top: 50, bottom: 50, left: 50, right: 50 };

    const svg = d3.select('#d3-container')
    .append('svg')
    .attr('width', width - margin.left - margin.right)
    .attr('height', height - margin.top - margin.bottom)
    .attr("viewBox", [0, 0, width, height]);

    const x = d3.scaleBand()
    .domain(d3.range(data.length))
    .range([margin.left, width - margin.right])
    .padding(0.3)

    const y = d3.scaleLinear()
    .domain([0, 100])
    .range([height - margin.bottom, margin.top])

    svg
    .append("g")
    .attr("fill", 'royalblue')
    .selectAll("rect")
    .data(data.sort((a, b) => d3.descending(a.score, b.score)))
    .join("rect")
        .attr("x", (d, i) => x(i))
        .attr("y", d => y(d.score))
        .attr('title', (d) => d.score)
        .attr("class", "rect")
        .attr("height", d => y(0) - y(d.score))
        .attr("width", x.bandwidth());

    function yAxis(g) {
    g.attr("transform", `translate(${margin.left}, 0)`)
        .call(d3.axisLeft(y).ticks(null, data.format))
        .padding(1)
        .attr("font-size", '20px')
    }

    function xAxis(g) {
    g.attr("transform", `translate(0,${height - margin.bottom})`)
        .call(d3.axisBottom(x).tickFormat(i => data[i].name))
        .attr("font-size", '20px')
    }

    svg.append("g").call(xAxis);
    svg.append("g").call(yAxis);
    svg.node();
    </script>
    </body>
    </html>
            
            
    X-Axis- Teams
    Y-Axis- Fund Spent in Crs     
        
        """ ,height=650)
