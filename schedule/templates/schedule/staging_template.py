
{% block bodycontent %}
<main class="">
  <section class="py-5 text-center container">
    <div class="custom-container container">
      <div class="custom-row row py-lg-5">
        <div class="col-lg-6 col-md-8 col-sm mx-auto">
          {% if show_instance_data %}
            <h1 class="custom-heading fs-1">{{ show_instance_data.archive_show_name }}</h1>
            <h2 class="custom-font text-warning"><span class="text-danger">Artist</span> || {{ show_instance_data.archive_artist_name }}</h2>
            <h3 class="custom-font text-warning"><span class="text-danger">Date</span> || {{ show_instance_data.archive_start_date }} <span class="text-danger">to</span> {{ show_instance_data.archive_end_date }}</h3>
          {% else %}
            <h1 class="custom-heading">Show Not Found</h1>
          {% endif %}
          <a href="{% url 'gallery-revolt' %}?open-past=true" class="custom-btn btn btn-danger custom-font">Back to Past</a>
        </div>
      </div>
    </div>
  </section>

  <div class="custom-album album py-5">
    <div class="custom-container container">
      <div class="custom-row row g-3">
        <!-- carousel start -->
        <div class="col-1"></div>
        <div class="col-10">
          <div class="custom-carousel-container container">
            <div id="imageCarousel" class="custom-carousel carousel slide" data-bs-ride="carousel">
              <div class="carousel-inner">
                {% for image in related_images %}
                  <div class="carousel-item {% if forloop.first %} active {% endif %}">
                    <div class="text-center">
                      <a href="https://live.staticflickr.com/{{ image.archive_image_server }}/{{ image.archive_image_id }}_{{ image.archive_image_secret }}.jpg">
                        <img src="https://live.staticflickr.com/{{ image.archive_image_server }}/{{ image.archive_image_id }}_{{ image.archive_image_secret }}.jpg" loading="lazy">
                      </a>
                    </div>
                  </div>

                  {% if forloop.counter|divisibleby:3 and not forloop.last %}
                    <div class="w-100"></div> <!-- Clears the float to start a new row -->
                  {% endif %}
                {% empty %}
                  <div class='text-center'>
                    <h2>No Images Available</h2>
                  </div>
                {% endfor %}
              </div>

              <button class="custom-carousel-control carousel-control-prev" type="button" data-bs-target="#imageCarousel" data-bs-slide="prev">
                <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                <span class="visually-hidden">Previous</span>
              </button>
              <button class="custom-carousel-control carousel-control-next" type="button" data-bs-target="#imageCarousel" data-bs-slide="next">
                <span class="carousel-control-next-icon" aria-hidden="true"></span>
                <span class="visually-hidden">Next</span>
              </button>
            </div>
          </div>
        </div>
        <div class="col-1"></div>
        <!-- carousel end -->
      </div>
    </div>
  </div>
</main>

{% endblock %}

{% block bodycontent %}
<main>
  <section class="py-5 text-center container">
    <div class="row py-lg-5">
      <div class="col-lg-6 col-md-8 mx-auto">
        {% if show_instance_data %}
          <h1>{{ show_instance_data.archive_show_name }}</h1>
          <p>{{ show_instance_data.archive_artist_name }}</p>
          <a href="{% url 'gallery-revolt' %}?open-past=true" class="custom-btn btn btn-danger custom-font mt-3 ps-3 pe-3 pt-2 pb-2">Back to Past</a>

        {% else %}
          <h1>Show Not Found</h1>
        {% endif %}
      </div>
    </div>
  </section>

  <div class="album py-5">
    <div class="container">
      <div class="row g-3">
        {% for image in related_images %}
          <div class="col ms-5 me-5">
            <div class="">
<a href="https://live.staticflickr.com/{{ image.archive_image_server }}/{{ image.archive_image_id }}_{{ image.archive_image_secret }}.jpg">
                        <img src="https://live.staticflickr.com/{{ image.archive_image_server }}/{{ image.archive_image_id }}_{{ image.archive_image_secret }}.jpg" loading="lazy">
                      </a>
            </div>
          </div>

        {% if forloop.counter|divisibleby:3 and not forloop.last %}
              <div class="w-100"></div> <!-- Clears the float to start a new row -->
            {% endif %}
        {% empty %}
          <div class='text-center'>
            <h2>No Images Available</h2>
          </div>
        {% endfor %}
      </div>
    </div>
  </div>
</main>





{% endblock %}