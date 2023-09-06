/*
var quiz = document.getElementById("quiz-form")
quiz.addEventListener("submit", formSubmission)

function formSubmission(e) {
    e.preventDefault();
    const selectedAnswer = document.querySelector('input[name="answer"]:checked');
        if (selectedAnswer) {
            const userAnswer = selectedAnswer.value;
            const correctAnswer = "{{ current_weather.country }}";  // Get the actual country from Jinja2

            if (userAnswer === correctAnswer) {
                alert('Correct! You guessed the right country.');
            } else {
                alert(`Incorrect. The correct answer is ` + correctAnswer);
            }
        } else {
            alert('Please select an answer.');
        }
};
*/