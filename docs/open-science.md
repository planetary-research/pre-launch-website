(open-science)=
:::{note}
This is a draft of the text that will appear on the journal website. To propose and discuss changes, please join the [online forum](#forum).
:::

# Open science: Data and software availability

*Planetary Reseach* supports the broad principles of open science, which include removing unnecessary barriers in academic publishing and promoting transparent and equitable practices (for example, see the [UNESCO Recommendation on Open Science](https://doi.org/10.54677/MNMH8546)). As a diamond open access journal, there are no financial barriers for authors to publish with us and all articles are free to access. Transparency of the peer-review process is assured by providing a review report for all accepted articles that includes the editor and reviewer assessments. Authors also retain the copyright to their work, which is by default licensed using the Creative Commons Attribution 4.0 license ([CC BY 4.0](https://creativecommons.org/licenses/by/4.0/deed.en)).

The journal strives to make all data, all significant derived datasets, and all numerical codes used in published articles available so that researchers may both verify and build upon the results of others. Data and software used in a manuscript should follow [FAIR principles](https://www.go-fair.org/fair-principles/), which means that they should be Findable, Accessible, Interoperable, and Reusable. The journal recognizes that every scientific domain has different needs and standards, and that any data and software availability policy will be necessarily incomplete. As a baseline, though, *Planetary Research* requires that all data used in a study, as well as any significant derived data products, be made freely available to the scientific community before an article is accepted for publication. Whenever possible, scientific codes should also be freely available, and when they are not, they must strictly adhere to the findability and accessibility requirements as outlined by [FAIR](https://www.go-fair.org/fair-principles/). Under no circumstance will the journal allow authors to promise to provide their data or software upon request.

The following sections provide further guidelines regarding the journal's requirements for data and software availability, and which public repositories should be used.

## Data availability

Articles published in the journal may contain at most a single PDF as a supplement. Any data that are not found in the manuscript and supplement must be uploaded to a public data repository before the article is accepted for publication. Even when the data are found in the manuscript (such as in a table), the authors may be asked to make the data accessible in a machine-readable format.

The datasets and any accompanying metadata and documentation must be made available to the reviewers during the peer-review process. In most cases this can be accomplished by providing a private link to a shared folder on a cloud storage platform. During the peer review process, the authors should explicitly cite these datasets in their manuscript using a provisional citation, and then update this citation at the time of final acceptance.

The authors should make available any data that a reasonable reader might ask for. The reviewers will be asked to assess whether the provided datasets and documentation are sufficient, and the editor will be the final arbiter as to which datasets are ultimately required. In general, datasets should include

* images presented in a manuscript, in both raw and processed formats,
* animations when individual time steps of a simulation are presented in a manuscript,
* tabular data used for creating any line graphs,
* machine readable forms of any tables in a manuscript,
* metadata and other documentation that are necessary for understanding the datasets, and
* any significant derived data products that are used as part of the scientific analysis.

If it is not feasible to provide all data, such as for a simulation with many time steps, the authors should provide the complete initialization files of the simulation so that the simulation could be later reproduced.

Datasets should be uploaded to a public repository that provides a persistent citable identifier, such as a DOI (digital object identifier). The data archive should contain a single file that describes the contents of the archive (such as a README or index.html file) and should contain a license that describes the conditions under which the data can be reused.

Each manuscript should contain a Data and Code Availability Statement at the end of the main text. This statement should mention any datasets used in the manuscript and how they can be accessed. This statement should also mention and cite any online datasets that accompany the article.

## Software availability

Software and numerical codes often play integral roles in scientific studies, and the reader should thus have access to fundamental information about these tools. Such software and codes could be open source and freely available, available with a commercial license, or require appropriate credentials to access. The journal does not require all source code to be freely available, only that the source code be as open as is allowed.

In general, the journal will ask that all specialized numerical codes that were developed as part of a submitted manuscript be made freely available in a public repository. When portions of the source code can not be made available (such as for commercial and restricted codes), it must be possible to point to documentation that describes the principles and numerical techniques used by the code. Even when the source code is not available, it should be possible to provide any modules that were written by the authors, or any initialization files that were used when running their simulations. When uploading code to a repository, the author must include a license that describes how the work can be reused by others.

Numerical codes must both be findable and accessible according to [FAIR principles](https://www.go-fair.org/fair-principles/). Findable means that the code can be located using a persistent identifier (such as a DOI) or a permanent URL. Github and Gitlab repositories can be deleted and are not considered as a being persistent. Software and codes that have a website with a root domain or that have a permanent institutional URL may be considered to be findable, but a persistent identifier is always preferable. URLs that are part of a personal website or that point to Github repositories are not acceptable.

The conditions under which the code and software can be accessed must be described either on the landing page of the code or in the code archive. For free and open source software, it is only necessary to include a copy of the license with the code. On the other hand, if the code is restricted and requires credentials to be accessed, the exact conditions under which the credentials can be obtained should be provided.

## Data and software repositories

Data and numerical codes should be uploaded to an appropriate repository. For datasets that will be used by large portions of the planetary science community (such as spacecraft data), a disciplinary data repository may be the best solution. For more ordinary datasets that accompany a manuscript, institutional, national, or general repositories would be appropriate.

The journal does not enforce the use of any specific repository. Nevertheless, for the case of ordinary data that are generated or used in a manuscript, we recommend [Zenodo](zenodo.org). The journal manages the [Planetary Research (journal)](https://zenodo.org/communities/planetary-research-org) community at Zenodo, which provides better visibility to author provided datasets and that provides an extra assurance of quality control. Datasets can be uploaded directly from our Zenodo community page, or can be uploaded to your individual account and then later submitted to the community. After submission to the Zenodo community, approval will be given after assuring that the datasets satisfy the journal's open science policies and standards.
