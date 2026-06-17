# CI/CD Pipeline Reflection

**1. What does each stage of your pipeline (lint, test, deploy) actually protect against?**
The `lint` stage protects against messy, unreadable code and syntax inconsistencies, ensuring a uniform code style across the team. The `test` stage protects against logical bugs and broken features by verifying that the application behaves as expected. Finally, the `deploy` stage ensures that only code that has passed all quality and functionality checks actually reaches the production environment.

**2. Why does the order matter — what could go wrong if `deploy` ran before `test`?**
The order is critical because it acts as a filter. If `deploy` ran before `test`, any broken code or severe bugs would be pushed directly to live users. Testing after deployment defeats the purpose of a quality gate, as the damage to the production environment would already be done.

**3. What's one thing you'd add to make this pipeline closer to a real production setup?**
To make this closer to a real production setup, I would replace the simulated echo deployment with an actual deployment step that pushes the application to a cloud hosting platform (like AWS, Render, or Railway) using secure GitHub Secrets for API keys.