(open-science)=
:::{note}
This is a draft of the text that will appear on the journal website. To propose and discuss changes, please join the [online forum](#forum).
:::

# Open science: Data and software availability

*Planetary Reseach* supports the broad principles of open science, which include removing unnecessary barriers in academic publishing and promoting transparent and equitable practices (for example, see the [UNESCO Recommendation on Open Science](https://doi.org/10.54677/MNMH8546)). As a diamond open access journal, there are no financial barriers for authors to publish with us and all articles are free to access. Transparency of the peer-review process is assured by providing a review report for all accepted articles that includes the editor and reviewer assessments. Authors also retain the copyright to their work, which is by default licensed using the Creative Commons Attribution 4.0 license ([CC BY 4.0](https://creativecommons.org/licenses/by/4.0/deed.en)).

The journal strives to make all data, all significant derived datasets, and all numerical codes used in published articles available so that researchers may both verify and build upon the results of others. Data and software used in a manuscript should follow [FAIR principles](https://www.go-fair.org/fair-principles/), which means that they should be Findable, Accessible, Interoperable, and Reusable. Each manuscript should furthermore contain a Data and Code Availability Statement. This statement should mention all datasets and numerical codes that were used or generated by the study and how they can be accessed.

The journal recognizes that every scientific domain has different needs and standards, and that any data and software availability policy will be necessarily incomplete. As a baseline, though, *Planetary Research* requires that all data used in a study, as well as any significant derived data products, be made freely available to the scientific community before an article is accepted for publication. Whenever possible, scientific codes should also be freely available, and when they are not, they must strictly adhere to the findability and accessibility requirements as outlined by [FAIR](https://www.go-fair.org/fair-principles/). Under no circumstance will the journal allow authors to promise to provide their data or software upon request.

The following sections provide further guidelines regarding the journal's requirements for data and software availability, as well as recommendations on which public repositories should be used.

## Data availability

Articles published in the journal may contain at most a single PDF as a supplement. Any data that were used or generated as part of the study and that are not found in the manuscript and supplement must be uploaded to a public data repository before the article is accepted for publication. Even when the data are found in the manuscript (such as in a table), the authors may be asked to make the data accessible in a machine-readable format.

The authors should make available any data that a reasonable reader might ask for. The reviewers will be asked to assess whether the provided datasets and documentation are sufficient, and the editor will be the final arbiter as to which datasets are ultimately required. In general, datasets should include

* images presented in a manuscript, in both raw and processed formats,
* animations when individual time steps of a simulation are presented in a manuscript,
* tabular data used for creating any line graphs,
* machine readable forms of any tables in a manuscript,
* metadata and other documentation that are necessary for understanding the datasets, and
* any significant derived data products that are used as part of the scientific analysis.

If it is not feasible to provide all data, such as for a simulation with many time steps, the authors should provide the complete initialization files of the simulation so that the simulation could be later reproduced.

The datasets and any accompanying metadata and documentation need to be made available to the reviewers during the peer-review process. When possible, the datasets should be shared from the repository where they will be ultimately published using a private link. For simplicity, the journal will also accept a private link to a shared folder on a cloud storage platform. During the peer review process, the authors should explicitly cite these datasets in their manuscript using a provisional citation and then update this citation at the time of final acceptance.

Datasets should be uploaded to a public repository that provides a persistent citable identifier, such as a DOI (digital object identifier). The data archive should contain a file that describes the contents of the archive (such as a README or index.html file) and should contain a license that describes the conditions under which the data can be reused.

## Software availability

Software and numerical codes often play an integral role in a scientific study, and the reader should thus have access to fundamental information about these tools. Software and numerical codes may be open source and freely available, available with a commercial license, or require appropriate credentials to access. The journal does not require all source code to be freely available, only that the source code be as open as is allowed.

In general, the journal will ask that all specialized numerical codes that were developed as part of a submitted manuscript be made freely available in a public repository. When portions of the source code can not be made available (such as for commercial and restricted codes), one must point to documentation that describes the principles and numerical techniques used by the code. Even when the primary source code is restricted, however, it should be possible to provide any modules that were written by the authors, or any initialization files that were used when running their simulations.

Numerical codes must both be findable and accessible according to [FAIR principles](https://www.go-fair.org/fair-principles/). Findable means that the code can be located using a persistent identifier, such as a software heritage identifier [SWHID](https://www.softwareheritage.org/), an astrophysics source code library identifier [ASCL](https://ascl.net/), or a DOI. Citations to Github and Gitlab repositories are not allowed as the repositories can be deleted at any time. Many of the codes on these platforms, however, are already archived by Software Heritage, and for those that aren't, the process of obtaining an SWHID is simple. If a commercial code does not have a persistent identifier, it should be cited using the guidelines provided by the software provider.

The conditions under which code and software used in a manuscript can be accessed must be described either on the landing page of the code or in the code archive. For free and open source software, it is only necessary to include a copy of the license with the code. On the other hand, if the code is restricted and requires credentials to be accessed, the exact conditions under which the credentials can be obtained should be provided.

## Data and software repositories

Data and numerical codes should be uploaded to the repository that is the most appropriate for the community that will use these products. For datasets that will be used by large portions of the planetary science community (such as spacecraft data), or for datasets that are part of a larger program, a disciplinary data repository may be the best solution (see the Registry of Research Data Repositories, [re3data](https://www.re3data.org/)). For more ordinary datasets that accompany a manuscript, institutional, national, or general repositories that assign a persistent identifier are usually appropriate.

The journal does not enforce the use of any specific data or code repository. Nevertheless, for the case of ordinary data that are generated or used in a manuscript, we recommend the [Planetary Research (journal)](https://zenodo.org/communities/planetary-research-org) community at [Zenodo](zenodo.org). This community only curates datasets that are part of Planetary Research publications. Datasets submitted to this community will be approved only after undergoing a quality control to assure that they meet the journal's standards. As for numerical codes, given its simplicity, the journal recommends obtaining a SWHID.
