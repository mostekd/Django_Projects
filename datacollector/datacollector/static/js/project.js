/* Project specific Javascript goes here. */

async function deleteUserSubmission(id) {
  if (!confirm('Czy na pewno chcesz usunąć ten wiersz?')) return;
  const response = await fetch(`/users/api/submissions/${id}/`, {
    method: 'DELETE',
    headers: { 'X-CSRFToken': getCookie('csrftoken') }
  });
  if (response.ok) {
    loadUsers(lastFilters.name, lastFilters.city, lastFilters.year, currentPage);
  } else {
    alert('Błąd podczas usuwania!');
  }
}

function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== '') {
    const cookies = document.cookie.split(';');
    for (let i = 0; i < cookies.length; i++) {
      const cookie = cookies[i].trim();
      if (cookie.substring(0, name.length + 1) === (name + '=')) {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}
