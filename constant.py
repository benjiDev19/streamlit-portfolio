import pandas as pd

edu = [['Master','CS','2024','Wuhan Textile University','N/A'],['Bachelor','CS','2022','Jiangxi University Of Technology', '3.63 GPA'],['12th(Baccalaureat)','Science','2016','Thomas Sankara A','12.39']]

skill_col_size = 5

embed_component= {'linkedin':"""<script src="https://platform.linkedin.com/badges/js/profile.js" async defer type="text/javascript"></script>
        <div class="badge-base LI-profile-badge" data-locale="en_US" data-size="large" data-theme="dark" data-type="HORIZONTAL" data-vanity="benjamin-a-83a153201" data-version="v1"><a class="badge-base__link LI-simple-link" href="https://cn.linkedin.com/in/benjamin-a-83a153201?trk=profile-badge">Benjamin A.</a></div>""", 'medium':"""<div style="overflow-y: scroll; height:500px;"> <div id="retainable-rss-embed"
data-rss="https://medium.com/feed/retainable,https://medium.com/feed/@benjaminampouala"
data-maxcols="3"
data-layout="grid"
data-color="green"
data-poststyle="inline"
data-readmore="Read more"
data-buttonclass="btn btn-primary"
data-offset="0"></div></div> <script src="https://www.twilik.com/assets/retainable/rss-embed/retainable-rss-embed.js"></script>"""}



info = {'name':'Ben AMPOUALA--benjiDev</>','bio':'Hi! I\'m Benjamin, a Software developer with over 3 years of experience, proficient in a variety of programming languages like Python, Java, Kotlin, Dart and technologies like AI. As a developer, I have worked on multiple projects, and excel at problem-solving and collaborating with cross-functional teams.I am highly organized, detail-oriented, and have strong communication. I\'m content and top writter at Medium, and time management skills.I\'m constantly seeking to learn and grow as a developer.','Stackoverflow_flair':'''<a href="https://stackoverflow.com/users/13606559/benjidev"><img src="https://stackoverflow.com/users/flair/13606559.png" width="208" height="58" alt="profile for benjiDev at Stack Overflow, Q&amp;A for professional and enthusiast programmers" title="profile for benjiDev at Stack Overflow, Q&amp;A for professional and enthusiast programmers"></a>''', 'LinkedIn_badge':'''<script src="https://platform.linkedin.com/badges/js/profile.js" async defer type="text/javascript"></script>''','skills':['Python','RDBMS','Firebase','JAVA','Kotlin','HTML & CSS','WordPress','Dart','Flutter','NodeJs','Streamlit','Flask','Pytorch','Tensorflow','Machine Learning'],'edu':pd.DataFrame(edu,columns=['Qualification','Stream','Year','Institute','Score']),'achievements':['Top AI writer @ Medium with 100+ blogs','1.8k+ reputation points on Stackoverflow','Guest speaker, Neo4j','TCS humAIn Finalist,2019','Shikshan Bharati Kulapati K.M. Munshi Award in Mathematics,2014','Bharatiya Vidya Bhavan Shri C. Subramaniam Award for excellence in character, 2009 & 2012','Certificate of Merit(Proficiency in Co-curricular activities) for Declamation and Extempore'],'Medium':'https://medium.com/@benjaminampouala','publication_url':"https://medium.com/@benjaminampouala/list/explore-the-ai-world-with-benjamin-73783cf178b3"}