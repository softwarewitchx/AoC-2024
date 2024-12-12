import fs from "fs";

const countXmasOccurrences = (inputFilePath) => {
  const xmasMatrix = [];

  try {
    const text = fs.readFileSync(inputFilePath, "utf8");
    if (!text) return 0;

    const rows = text.trim().split("\n");

    for (const row of rows) {
      xmasMatrix.push(row.split(""));
    }

    let xmasCounter = 0;

    for (let i = 0; i < xmasMatrix.length; i++) {
      for (let j = 0; j < xmasMatrix[i].length; j++) {
        const currentChar = xmasMatrix[i][j];

        if (xmasMatrix?.[i - 3]?.[j - 3]) {
          const topLeftDiagonal =
            currentChar +
            xmasMatrix[i - 1][j - 1] +
            xmasMatrix[i - 2][j - 2] +
            xmasMatrix[i - 3][j - 3];

          if (topLeftDiagonal === "XMAS") xmasCounter++;
        }

        if (xmasMatrix?.[i - 3]?.[j + 3]) {
          const topRightDiagonal =
            currentChar +
            xmasMatrix[i - 1][j + 1] +
            xmasMatrix[i - 2][j + 2] +
            xmasMatrix[i - 3][j + 3];

          if (topRightDiagonal === "XMAS") xmasCounter++;
        }

        if (xmasMatrix?.[i + 3]?.[j - 3]) {
          const botLeftDiagonal =
            currentChar +
            xmasMatrix[i + 1][j - 1] +
            xmasMatrix[i + 2][j - 2] +
            xmasMatrix[i + 3][j - 3];

          if (botLeftDiagonal === "XMAS") xmasCounter++;
        }

        if (xmasMatrix?.[i + 3]?.[j + 3]) {
          const botRightDiagonal =
            currentChar +
            xmasMatrix[i + 1][j + 1] +
            xmasMatrix[i + 2][j + 2] +
            xmasMatrix[i + 3][j + 3];

          if (botRightDiagonal === "XMAS") xmasCounter++;
        }

        if (xmasMatrix[i]?.[j - 3]) {
          const left =
            currentChar +
            xmasMatrix[i][j - 1] +
            xmasMatrix[i][j - 2] +
            xmasMatrix[i][j - 3];

          if (left === "XMAS") xmasCounter++;
        }

        if (xmasMatrix[i]?.[j + 3]) {
          const right =
            currentChar +
            xmasMatrix[i][j + 1] +
            xmasMatrix[i][j + 2] +
            xmasMatrix[i][j + 3];

          if (right === "XMAS") xmasCounter++;
        }

        if (xmasMatrix?.[i - 3]?.[j]) {
          const top =
            currentChar +
            xmasMatrix[i - 1][j] +
            xmasMatrix[i - 2][j] +
            xmasMatrix[i - 3][j];

          if (top === "XMAS") xmasCounter++;
        }

        if (xmasMatrix?.[i + 3]?.[j]) {
          const bot =
            currentChar +
            xmasMatrix[i + 1][j] +
            xmasMatrix[i + 2][j] +
            xmasMatrix[i + 3][j];

          if (bot === "XMAS") xmasCounter++;
        }
      }
    }
    return xmasCounter;
  } catch (err) {
    console.error(err);
  }
};

const totalXmasOccurrences = countXmasOccurrences("./puzzle-input.txt");
console.log(totalXmasOccurrences);
