<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>

<!-- PROJECT LOGO -->
<br />
<!--<div align="center">
  <a href="https://github.com/github_username/repo_name">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a> -->

<h1 align="center">From Black Box to Glass Box: The Impact of Data Complexity on Machine Learning Explainability</h1>
<h2 align="center">A Senior Thesis for the ORFE Department at Princeton University</h2>
<h2 align="center">Melissa Woo, Princeton 2024</h2>
<h2 align="center">Advised by: Dr. Margaret Holen</h2>

  <p align="left">
    Abstract: Advancements in machine learning (ML) have sparked innovation across the finance sector, introducing the use of sophisticated models in critical areas like credit scoring and risk assessment. While powerful, these models often operate as ``black boxes," with opaque decision-making that raises significant concerns about fairness and accountability. 
This has spurred much research in ML explainability and particularly in post-hoc feature attribution methods, which aim to clarify model decisions by assessing the influence of each input feature on the outcome. With the rapid proliferation of such methods, performance evaluation across different feature attribution methods is key, but requires detailed, context-specific insights, making it difficult to apply conclusions broadly across different use cases. In our research, we develop an evaluation framework to assess explanation faithfulness across varying complexities of both data and ML models. Using synthetically generated data, we show the varying impact of feature correlation, target expression complexity, and on/off-manifold scenarios on the performance of popular post-hoc feature attribution methods. Despite degrading explanation faithfulness with increasing data complexity, post-hoc feature attribution methods consistently outperform direct model explanations, enhancing ML models of all complexities, including simpler ones often perceived as self-contained. Analyzing each method's performance over diverse contexts reveals distinct strengths and weaknesses. While LIME and MAPLE effectively extrapolate explanations for data from unseen distributions, they encounter difficulties with highly correlated, nonlinear data. Conversely, On-Manifold SHAP, followed by SHAP and KernelSHAP, excel at explaining data that mirrors the training distribution, even for high complexity. These findings offer actionable insights for both practitioners and researchers in method selection and development alike.
    <br />
    <br />
    <a href="[https://github.com/github_username/repo_name](https://github.com/melissaw203/posthoc_method_eval/)"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/github_username/repo_name">View Demo</a>
    ·
    <a href="https://github.com/github_username/repo_name/issues/new?labels=bug&template=bug-report---.md">Report Bug</a>
    ·
    <a href="https://github.com/github_username/repo_name/issues/new?labels=enhancement&template=feature-request---.md">Request Feature</a>
  </p>
</div>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* [My thesis advisor Dr. Margaret Holen for her invaluable help and support in this endeavor.]()
* []()
* []()

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/github_username/repo_name.svg?style=for-the-badge
[contributors-url]: https://github.com/github_username/repo_name/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/github_username/repo_name.svg?style=for-the-badge
[forks-url]: https://github.com/github_username/repo_name/network/members
[stars-shield]: https://img.shields.io/github/stars/github_username/repo_name.svg?style=for-the-badge
[stars-url]: https://github.com/github_username/repo_name/stargazers
[issues-shield]: https://img.shields.io/github/issues/github_username/repo_name.svg?style=for-the-badge
[issues-url]: https://github.com/github_username/repo_name/issues
[license-shield]: https://img.shields.io/github/license/github_username/repo_name.svg?style=for-the-badge
[license-url]: https://github.com/github_username/repo_name/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/linkedin_username
[product-screenshot]: images/screenshot.png
[Next.js]: https://img.shields.io/badge/next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white
[Next-url]: https://nextjs.org/
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/
[Vue.js]: https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D
[Vue-url]: https://vuejs.org/
[Angular.io]: https://img.shields.io/badge/Angular-DD0031?style=for-the-badge&logo=angular&logoColor=white
[Angular-url]: https://angular.io/
[Svelte.dev]: https://img.shields.io/badge/Svelte-4A4A55?style=for-the-badge&logo=svelte&logoColor=FF3E00
[Svelte-url]: https://svelte.dev/
[Laravel.com]: https://img.shields.io/badge/Laravel-FF2D20?style=for-the-badge&logo=laravel&logoColor=white
[Laravel-url]: https://laravel.com
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[JQuery.com]: https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white
[JQuery-url]: https://jquery.com 
