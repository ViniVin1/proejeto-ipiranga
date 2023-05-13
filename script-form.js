const form = document.getElementById('form-pesquisa');

    form.addEventListener('submit', (event) => {
      event.preventDefault();
      
      const formData = new FormData(form);

      fetch('http://127.0.0.1:5000/pesquisa', {
        method: 'POST',
        body: JSON.stringify(Object.fromEntries(formData)),
        headers: {
          'Content-Type': 'application/json'
        }
      })
      .then(response => response.json())
      .then(data => {
        alert(data.mensagem);
        form.reset();
      })
      .catch(error => console.error(error));
    });