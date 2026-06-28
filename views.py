from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Question, Choice, Submission


@login_required
def submit(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choices.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        messages.error(request, 'You did not select a valid choice.')
        return redirect('detail', question_id=question.id)
    else:
        submission, created = Submission.objects.update_or_create(
            question=question,
            user=request.user,
            defaults={'selected_choice': selected_choice}
        )
        selected_choice.votes += 1
        selected_choice.save()
        messages.success(request, 'Your answer has been recorded.')
        return redirect('results', question_id=question.id)


@login_required
def show_exam_result(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        submission = Submission.objects.get(question=question, user=request.user)
    except Submission.DoesNotExist:
        messages.info(request, 'You have not submitted an answer for this question yet.')
        return redirect('detail', question_id=question.id)

    total_votes = sum(c.votes for c in question.choices.all())
    context = {
        'question': question,
        'submission': submission,
        'total_votes': total_votes,
    }
    return render(request, 'onlinecourse/results.html', context)
