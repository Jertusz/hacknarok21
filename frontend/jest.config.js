module.exports = {
  preset: "@vue/cli-plugin-unit-jest/presets/typescript-and-babel",
  verbose: true,
  reporters: [
    "default",
    [
      "jest-stare",
      {
        resultDir: "results/jest-stare",
        reportTitle: "jest-stare!",
        additionalResultsProcessors: ["jest-junit"],
        coverageLink: "../../coverage/lcov-report/index.html",
      },
    ],
  ],
  collectCoverage: true,
  collectCoverageFrom: ["src/**/*.{ts}", "!src/main.ts"],
  transform: {
    "^.+\\.vue$": "vue-jest"
  }
};
