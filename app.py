import streamlit as st 
import numpy
import pickle

prmodel = pickle.load(open("salarypr_model.pickle",'rb'))


def model(*args):
	prediction = prmodel.predict([args])
	print(prediction)
	return prediction

def main():	
	st.title("SALARY PREDICTION")
	html_temp = """<div style ="background-color:grey;padding:10px">
	<h2 style = "color:black;text-allign:center;"> FILL REQUIRED TEXTBOX TO CHECK YOUR SALARY </h2>
	</div>
	"""
	st.markdown(html_temp,unsafe_allow_html= True)
	age = st.text_input("age"," ")
	test_score		= st.text_input("test_score_out_of_10"," ")
	interview_score	= st.text_input("interview_score_out_of_10"," ")

	result = ""	
	if st.button("PREDICT"):
		result = model(int(age),int(test_score),int(interview_score))
	
	val = result[0].round()
	st.success(f" THE PREDICTED/SUGGESTED SALARY IS {val}")

	if st.button("ABOUT"):
		st.text("THIS WEBAPP PREDICTS THE SALARY BASED UPON YOUR AGE,TEST/INTERVIEW SCORES")


if __name__ == "__main__":
	main()

