console.log("test");
const el = document.getElementById("h5p-container");
const options = {
  h5pJsonPath: "/interactive-video",
  frameJs: "/assets/dist/frame.bundle.js",
  frameCss: "/assets/styles/h5p.css",
};

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
        body: JSON.stringify({ score: score, maxScore: maxScore }),
      }).catch(error => console.error('Error:', error));
    }
  });
});
