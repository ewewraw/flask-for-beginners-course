<html>
<head>
<title>main2.py</title>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
<style type="text/css">
.s0 { color: #cc7832;}
.s1 { color: #a9b7c6;}
.s2 { color: #808080;}
.s3 { color: #6a8759;}
.s4 { color: #6897bb;}
</style>
</head>
<body bgcolor="#2b2b2b">
<table CELLSPACING=0 CELLPADDING=5 COLS=1 WIDTH="100%" BGCOLOR="#606060" >
<tr><td><center>
<font face="Arial, Helvetica" color="#000000">
main2.py</font>
</center></td></tr></table>
<pre><span class="s0">from </span><span class="s1">flask </span><span class="s0">import </span><span class="s1">Flask</span><span class="s0">, </span><span class="s1">render_template</span><span class="s0">, </span><span class="s1">redirect</span><span class="s0">, </span><span class="s1">url_for</span><span class="s0">, </span><span class="s1">request  </span><span class="s2"># include the flask library</span>
<span class="s0">import </span><span class="s1">locale</span>
<span class="s0">import </span><span class="s1">json</span>
<span class="s0">import </span><span class="s1">os</span>
<span class="s0">from </span><span class="s1">os </span><span class="s0">import </span><span class="s1">listdir</span>
<span class="s0">from </span><span class="s1">os.path </span><span class="s0">import </span><span class="s1">isfile</span><span class="s0">, </span><span class="s1">join</span>
<span class="s0">from </span><span class="s1">flask_mail </span><span class="s0">import </span><span class="s1">Mail</span><span class="s0">, </span><span class="s1">Message</span>
<span class="s0">import </span><span class="s1">locale</span>
<span class="s0">from </span><span class="s1">flask_mail </span><span class="s0">import </span><span class="s1">Mail</span><span class="s0">, </span><span class="s1">Message</span>
<span class="s0">import </span><span class="s1">json</span>
<span class="s0">from </span><span class="s1">os </span><span class="s0">import </span><span class="s1">listdir</span>
<span class="s0">from </span><span class="s1">os.path </span><span class="s0">import </span><span class="s1">isfile</span><span class="s0">, </span><span class="s1">join</span>
<span class="s0">from </span><span class="s1">flask_mail </span><span class="s0">import </span><span class="s1">Mail</span><span class="s0">, </span><span class="s1">Message</span>
<span class="s0">import </span><span class="s1">os</span>

<span class="s1">app = Flask(__name__)</span>

<span class="s1">app.config[</span><span class="s3">'MAIL_SERVER'</span><span class="s1">] = </span><span class="s3">'smtp.gmail.com'</span>
<span class="s1">app.config[</span><span class="s3">'MAIL_PORT'</span><span class="s1">] = </span><span class="s4">465</span>
<span class="s2"># TODO: replace with your email</span>
<span class="s1">app.config[</span><span class="s3">'MAIL_USERNAME'</span><span class="s1">] = os.getenv(</span><span class="s3">&quot;FROM_EMAIL&quot;</span><span class="s1">)</span>
<span class="s2"># TODO:</span>
<span class="s2"># The following line should contain a password set in app passwords ion your google account.</span>
<span class="s2"># The password itself should be stored in .env file. DO NOT PUSH YOUR .env FILE TO GIT!!!</span>
<span class="s2"># Look at the example in .dummy-env. This is how your .env should look like</span>
<span class="s1">app.config[</span><span class="s3">'MAIL_PASSWORD'</span><span class="s1">] = os.getenv(</span><span class="s3">&quot;EMAIL_PASSWORD&quot;</span><span class="s1">)</span>
<span class="s1">app.config[</span><span class="s3">'MAIL_USE_TLS'</span><span class="s1">] = </span><span class="s0">False</span>
<span class="s1">app.config[</span><span class="s3">'MAIL_USE_SSL'</span><span class="s1">] = </span><span class="s0">True</span>

<span class="s1">mail = Mail(app)</span>

<span class="s1">app_language = </span><span class="s3">'ru_RU'</span>

<span class="s1">@app.route(</span><span class="s3">'/portfolio'</span><span class="s1">)</span>
<span class="s0">def </span><span class="s1">main_page():</span>
    <span class="s2">#app_language</span>
    <span class="s2"># TODO</span>
    <span class="s2"># Look at the translations argument. How does it look like?</span>
    <span class="s2"># What kind of object is that? What is inside?</span>
    <span class="s2"># Maybe you can print it and have a look?</span>
    <span class="s2"># TODO: Main task: 1) make everything translatable 2) add another language (any)</span>
    <span class="s0">return </span><span class="s1">render_template(</span><span class="s3">'portfolio.html'</span><span class="s0">, </span><span class="s1">translations=languages.get(app_language))</span>

<span class="s1">@app.route(</span><span class="s3">'/dummy_function'</span><span class="s0">, </span><span class="s1">methods = [</span><span class="s3">'POST'</span><span class="s1">])</span>
<span class="s0">def </span><span class="s1">dummy_function():</span>
    <span class="s0">global </span><span class="s1">app_language</span>
    <span class="s2"># TODO</span>
    <span class="s2"># what is this weird function?</span>
    <span class="s1">lang = request.form[</span><span class="s3">'lang'</span><span class="s1">]</span>
    <span class="s1">print(</span><span class="s3">'shiiish'</span><span class="s1">)</span>
    <span class="s1">print(lang)</span>
    <span class="s1">print(</span><span class="s3">&quot;button clicked&quot;</span><span class="s1">)</span>
    <span class="s0">if </span><span class="s1">lang == </span><span class="s3">'en'</span><span class="s1">:</span>
        <span class="s1">app_language = </span><span class="s3">'en_EN'</span>
        <span class="s0">return </span><span class="s1">render_template(</span><span class="s3">'portfolio.html'</span><span class="s0">, </span><span class="s1">translations=languages.get(app_language))</span>
    <span class="s0">elif </span><span class="s1">lang == </span><span class="s3">'ru'</span><span class="s1">:</span>
        <span class="s1">app_language = </span><span class="s3">'ru_RU'</span>
        <span class="s0">return </span><span class="s1">render_template(</span><span class="s3">'portfolio.html'</span><span class="s0">, </span><span class="s1">translations=languages.get(app_language))</span>
    <span class="s0">else</span><span class="s1">:</span>
        <span class="s1">app_language = </span><span class="s3">'ch_CH'</span>
        <span class="s0">return </span><span class="s1">render_template(</span><span class="s3">'portfolio.html'</span><span class="s0">, </span><span class="s1">translations=languages.get(app_language))</span>
<span class="s1">@app.route(</span><span class="s3">'/volunteering_activity'</span><span class="s1">)</span>
<span class="s0">def </span><span class="s1">volunteering_activity():</span>
    <span class="s0">return </span><span class="s1">render_template(</span><span class="s3">'examples_of_works.html'</span><span class="s0">, </span><span class="s1">translations=languages.get(app_language))</span>

<span class="s1">@app.route(</span><span class="s3">'/education'</span><span class="s1">)</span>
<span class="s0">def </span><span class="s1">education():</span>
    <span class="s0">return </span><span class="s1">render_template(</span><span class="s3">'education.html'</span><span class="s0">, </span><span class="s1">translations=languages.get(app_language))</span>

<span class="s1">@app.route(</span><span class="s3">'/biography'</span><span class="s1">)</span>
<span class="s0">def </span><span class="s1">information():</span>
    <span class="s0">return </span><span class="s1">render_template(</span><span class="s3">'biography.html'</span><span class="s0">, </span><span class="s1">translations=languages.get(app_language))</span>

<span class="s1">@app.route(</span><span class="s3">'/working_experience'</span><span class="s1">)</span>
<span class="s0">def </span><span class="s1">working_experience():</span>
    <span class="s0">return </span><span class="s1">render_template(</span><span class="s3">'working_experience.html'</span><span class="s0">, </span><span class="s1">translations=languages.get(app_language))</span>

<span class="s1">@app.route(</span><span class="s3">'/hobbies'</span><span class="s1">)</span>
<span class="s0">def </span><span class="s1">hobbies():</span>
    <span class="s0">return </span><span class="s1">render_template(</span><span class="s3">'hobbies.html'</span><span class="s0">, </span><span class="s1">translations=languages.get(app_language))</span>

<span class="s1">@app.route(</span><span class="s3">&quot;/send-test-email&quot;</span><span class="s0">, </span><span class="s1">methods = [</span><span class="s3">'POST'</span><span class="s1">])</span>
<span class="s0">def </span><span class="s1">index():</span>
    <span class="s1">firstname = request.form[</span><span class="s3">'firstname'</span><span class="s1">]</span>
    <span class="s1">lastname = request.form[</span><span class="s3">'lastname'</span><span class="s1">]</span>
    <span class="s1">message = request.form[</span><span class="s3">'message'</span><span class="s1">]</span>
    <span class="s1">email = request.form[</span><span class="s3">'email'</span><span class="s1">]</span>
    <span class="s1">msg = Message(</span><span class="s3">'New email from' </span><span class="s1">+ </span><span class="s3">' ' </span><span class="s1">+ firstname + </span><span class="s3">' ' </span><span class="s1">+ lastname</span><span class="s0">, </span><span class="s1">sender=request.form[</span><span class="s3">'email'</span><span class="s1">]</span><span class="s0">, </span><span class="s1">recipients=[</span><span class="s3">'ira1807001@gmail.com'</span><span class="s1">])</span>
    <span class="s1">msg.body = request.form[</span><span class="s3">'message'</span><span class="s1">]</span>
    <span class="s1">mail.send(msg)</span>
    <span class="s1">msg1 = Message(</span><span class="s3">'Dear,' </span><span class="s1">+ </span><span class="s3">' ' </span><span class="s1">+ firstname + </span><span class="s3">' ' </span><span class="s1">+ </span><span class="s3">', ' </span><span class="s1">+ </span><span class="s3">'your message is sent!'</span><span class="s0">, </span><span class="s1">sender=</span><span class="s3">'ira1807001@gmail.com'</span><span class="s0">, </span><span class="s1">recipients=[request.form[</span><span class="s3">'email'</span><span class="s1">]])</span>
    <span class="s1">mail.send(msg1)</span>
    <span class="s0">return </span><span class="s3">&quot;Your message is sent!&quot;</span>

<span class="s0">def </span><span class="s1">get_stats(input):</span>
    <span class="s0">return </span><span class="s1">locale.format_string(</span><span class="s3">'%d'</span><span class="s0">, </span><span class="s1">input)</span>


<span class="s0">def </span><span class="s1">get_currencies(input):</span>
    <span class="s0">return </span><span class="s1">locale.currency(input</span><span class="s0">, </span><span class="s1">international=</span><span class="s0">True</span><span class="s1">)</span>

<span class="s0">if </span><span class="s1">__name__ == </span><span class="s3">'__main__'</span><span class="s1">:</span>
    <span class="s1">app_language = </span><span class="s3">'ru_RU'</span>
    <span class="s1">locale.setlocale(locale.LC_ALL</span><span class="s0">, </span><span class="s1">app_language)</span>
    <span class="s1">languages = {}</span>
    <span class="s2"># TODO: so we just took all the files that are in the language directory? Hmm..</span>
    <span class="s1">languages_list = [f </span><span class="s0">for </span><span class="s1">f </span><span class="s0">in </span><span class="s1">listdir(os.path.join(</span><span class="s3">&quot;.&quot;</span><span class="s0">, </span><span class="s3">'languages'</span><span class="s1">)) </span><span class="s0">if </span><span class="s1">isfile(join(os.path.join(</span><span class="s3">&quot;.&quot;</span><span class="s0">, </span><span class="s3">'languages'</span><span class="s1">)</span><span class="s0">, </span><span class="s1">f))]</span>
    <span class="s2"># [&quot;en_EN.json&quot;, &quot;ru_RU.json&quot;]</span>
    <span class="s2"># TODO: And for each file... ?</span>
    <span class="s0">for </span><span class="s1">lang </span><span class="s0">in </span><span class="s1">languages_list:</span>
        <span class="s2"># TODO: we extract the language code from the file name...</span>
        <span class="s1">lang_code = lang.split(</span><span class="s3">'.'</span><span class="s1">)[</span><span class="s4">0</span><span class="s1">]</span>
        <span class="s2"># TODO: and look inside the file</span>
        <span class="s0">with </span><span class="s1">open(os.path.join(</span><span class="s3">&quot;.&quot;</span><span class="s0">, </span><span class="s3">'languages'</span><span class="s0">, </span><span class="s1">lang)</span><span class="s0">, </span><span class="s3">'r'</span><span class="s0">, </span><span class="s1">encoding=</span><span class="s3">'utf8'</span><span class="s1">) </span><span class="s0">as </span><span class="s1">file:</span>
            <span class="s2"># TODO: and for our languages array we add the content of each file under the language code. Hmm...</span>
            <span class="s1">languages[lang_code] = json.loads(file.read())</span>
    <span class="s2"># TODO: So, how will the languages array look like in the end? Let's try to print it and see the console logs...</span>

    <span class="s1">app.run(host=</span><span class="s3">&quot;0.0.0.0&quot;</span><span class="s0">, </span><span class="s1">port=</span><span class="s4">8080</span><span class="s0">, </span><span class="s1">debug=</span><span class="s0">True</span><span class="s1">)  </span><span class="s2"># application will start listening for web request on port 5000</span>
</pre>
</body>
</html>