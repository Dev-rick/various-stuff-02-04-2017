# -*- coding: utf-8 -*-
import webapp2
import os
import jinja2
from datetime import datetime
import quiz



template_dir = os.path.join(os.path.dirname(__file__), "templates")
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir), autoescape=False)






class BaseHandler(webapp2.RequestHandler):
    def write(self, *a, **kw):
        return self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        return self.write(self.render_str(template, **kw))

    def render_template(self, view_filename, params=None):
        if not params:
            params = {}
        template = jinja_env.get_template(view_filename)
        return self.response.out.write(template.render(params))
    def get_time(self):
        now = datetime.now()
        time = "%s:%s:%s / %s.%s.%s" % (now.hour + 2, now.minute, now.second, now.day, now.month, now.year)
        return time




class MainPage(BaseHandler):
    def get(self):
        now = super(MainPage, self).get_time()
        params = {"time": now}
        return self.render_template("home.html", params=params)  # render_template holt sich diese Datei




class LotteryHandler(BaseHandler):
    def get(self):
        now = super(LotteryHandler, self).get_time()
        params = {"time": now}
        return self.render_template("lottery.html", params=params)  # render_template holt sich diese Datei

    def post(self):
        now = super(LotteryHandler, self).get_time()
        result = self.request.get("num")
        result1 = int(result)
        import Lottery
        list_of_numbers_int = Lottery.random_numbers(result1)
        params = {"list_of_numbers_int": list_of_numbers_int,"time": now}
        return self.render_template("gen_numbers.html", params=params)




class CalHandler(MainPage):
    def get(self):
        now = super(CalHandler, self).get_time()
        params = {"time": now}
        return self.render_template("calculator.html", params=params)  # render_template holt sich diese Datei

    def post(self):
        now = super(CalHandler, self).get_time()
        num1 = self.request.get("number1")
        num2 = self.request.get("number2")
        num1 = float(num1)
        num2 = float(num2)
        operation = self.request.get("operation")
        import adv_calculator
        result = adv_calculator.calculate(operation, num1, num2)
        params = {"result": result, "time": now}
        return self.render_template("calculator.html", params=params)




class GuessSecretNumberHandler(BaseHandler):
    def get(self):
        now = super(GuessSecretNumberHandler, self).get_time()
        params = {"time": now}
        return self.render_template("guess_secret_number.html", params=params)

    def post(self):
        now = super(GuessSecretNumberHandler, self).get_time()
        guess = self.request.get("guess")
        import secret_number
        result = secret_number.guess_the_secret_number(guess)
        if result == True:
            result = "You have won!!!"
        elif result == False:
            result = "You lost, try again!"
        params = {"time": now, "result": result}
        return self.render_template("guess_secret_number.html", params)




class ConverterToKmHandler(BaseHandler):
    def post(self):
        now = super(ConverterToKmHandler, self).get_time()
        import converter
        miles = self.request.get("miles")
        miles = float(miles)
        miles_in_km = converter.converter_miles_to_km(miles)
        miles_in_km = str(miles_in_km)
        params = {"time": now, "km": miles_in_km}
        self.render_template("converter.html", params)




class ConverterToMilesHandler(BaseHandler):
    def post(self):
        now = super(ConverterToMilesHandler, self).get_time()
        km = self.request.get("km")
        km = float(km)
        import converter
        km_in_miles = converter.converter_km_to_miles(km)
        km_in_miles = str(km_in_miles)
        params = {"time": now, "miles": km_in_miles}
        self.render_template("converter.html", params)




class QuizHandler(BaseHandler):
    def get(self):
        now = super(QuizHandler, self).get_time()
        country = quiz.get_random_capital(quiz.countrydict)
        capital_picture = quiz.get_capital_picture(country, quiz.capitalpicturedict)
        params = {"time": now, "question": country,"capital_picture": capital_picture}
        return self.render_template("quiz.html", params=params)  # render_template holt sich diese Datei

    def post(self):
        now = super(QuizHandler, self).get_time()
        user_capital = self.request.get("answer")
        country = self.request.get("country")
        result = quiz.check_result(country, user_capital, quiz.countrydict)
        new_country = quiz.get_random_capital(quiz.countrydict)
        capital_picture = quiz.get_capital_picture(country, quiz.capitalpicturedict)
        params = {"time": now, "result": result, "question": new_country, "capital_picture": capital_picture}
        return self.render_template("quiz.html", params=params)  # render_template holt sich diese Datei




class ConvertHandler(BaseHandler):
    def get(self):
        now = super(ConvertHandler, self).get_time()
        params = {"time": now}
        return self.render_template("converter.html", params=params)




class DNAHandler(BaseHandler):
    def get(self):
        now = super(DNAHandler, self).get_time()
        params = {"time": now}
        return self.render_template("csi.html", params=params)

    def post(self):
        now = super(DNAHandler, self).get_time()
        searched_dna = self.request.get("dna")
        criminal = []
        import dna_program
        result_gender = dna_program.result_gender(searched_dna, dna_program.genders, criminal)
        result_race = dna_program.result_race(searched_dna, dna_program.races, criminal)
        result_hair_color = dna_program.result_hair_color(searched_dna, dna_program.hair_colors, criminal)
        result_eye_color = dna_program.result_eye_color(searched_dna, dna_program.eye_colors, criminal)
        result_facial_shape = dna_program.result_facial_shape(searched_dna, dna_program.facial_shapes, criminal)
        result_suspect = dna_program.result_suspect(dna_program.suspects, criminal)
        params = {"time": now,
                  "gender": result_gender,
                  "race": result_race,
                  "hair_color": result_hair_color,
                  "eye_color": result_eye_color,
                  "facial_shape": result_facial_shape,
                  "suspect": result_suspect}

        return self.render_template("csi.html", params=params)






app = webapp2.WSGIApplication([
    ('/', MainPage),
    ("/lottery", LotteryHandler),
    ("/calculator", CalHandler),
    ("/guessthesecretnumber", GuessSecretNumberHandler),
    ("/converter", ConvertHandler),
    ("/converter_to_km", ConverterToKmHandler),
    ("/converter_to_miles", ConverterToMilesHandler),
    ("/quiz", QuizHandler),
    ("/lottery", LotteryHandler),
    ("/csi", DNAHandler),
], debug=True)

