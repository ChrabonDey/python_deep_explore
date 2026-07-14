const express = require("express");
const cors = require("cors");
const app = express();

app.use(
  cors({
    origin: "*",
    methods: ["GET", "POST", "QUERY", "OPTIONS"],
  }),
);
app.use(express.json());

app.use("/products", (req, res, next) => {
  if (req.method === "QUERY") {
    console.log("Method: ", req.method);
    console.log("Body: ", req.body);

    return res.json({
      success: true,
      message: "Query received successfully",
      filters: req.body,
    });
  }
  next();
});
// Normal GET
app.get("/products", (req, res) => {
  res.json({
    message: "This is GET request",
  });
});

app.listen(3000, () => {
  console.log("Server running on port 3000");
});
