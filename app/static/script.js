console.log("Initializing H5P content");
const el = document.getElementById("h5p-container");
const courseId = el.getAttribute("data-course-id");
const options = {
  h5pJsonPath: "/static/interactive-video", // Ensure this path is correct
  frameJs: "/static/assets/dist/frame.bundle.js",
  frameCss: "/static/assets/dist/styles/h5p.css",
};

if (typeof H5PStandalone !== "undefined") {
  new H5PStandalone.H5P(el, options).then(function () {
    H5P.externalDispatcher.on("xAPI", function (event) {
      if (event.getVerb() === "answered") {
        const score = event.getScore();
        const maxScore = event.getMaxScore();
        fetch("http://127.0.0.1:8000/log", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
            score: score,
            maxScore: maxScore,
            course_id: courseId,
          }),
        })
          .then((response) => {
            if (!response.ok) {
              throw new Error(`HTTP error! Status: ${response.status}`);
            }
            return response.json();
          })
          .then((data) => {
            console.log("Success:", data);
          })
          .catch((error) => {
            console.error("Error:", error);
          });
      }
    });
  });
} else {
  console.error("H5PStandalone is not defined");
}
