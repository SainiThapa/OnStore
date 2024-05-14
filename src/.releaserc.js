module.exports = {
  branches: [{ name: "master" }],
  tagFormat: "v${version}",
  plugins: [
    [
      "@semantic-release/commit-analyzer",
      {
        preset: "conventionalcommits",
        releaseRules: [
          { type: "refactor", release: "patch" },
          { type: "feat", release: "minor" },
          { type: "fix", release: "patch" },
          { type: "breaking", release: "major" },
          { type: "perf", release: "patch" },
        ],
      },
    ],
    [
      "@semantic-release/release-notes-generator",
      {
        preset: "conventionalcommits",
        presetConfig: {
          types: [
            { type: "feat", section: "Features" },
            { type: "fix", section: "Bug Fixes" },
            { type: "refactor", section: "Refactoring" },
            { type: "perf", section: "Performance improvements" },
          ],
        },
      },
    ],
    "@semantic-release/changelog",
    [
      "@semantic-release/git",
      {
        message:
          "chore(release): ${lastRelease.version} → ${nextRelease.version} [ci upload],
      },
    ],
  ],
};
