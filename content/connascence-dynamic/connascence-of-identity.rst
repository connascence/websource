Connascence of Identity
########################

:strength: 80
:slug: identity
:summary: Connascence of identity is when multiple components must reference the same entity.

Connascence of identity is when multiple components must reference the same entity. 

If the entity that is referenced changes then all of the components that reference it would need to change too.

For example:

- You have an Excel worksheet that acts as a data source for more than 1 report.

- This worksheet changes occasionally - it is replaced by a new version (with a different file name but the same structure). In other words, the identity of the worksheet you must reference has changed.

- Every time it changes you must remember to change the code in multiple places to reference the new worksheet.

- If you miss one of these changes your code will still compile and produce results. 

- You will only notice the mistake once your users report data disparity issues across their reports.

.. code-block:: cs

    // Somewhere in the codebase we find this
    public List<SalesReportLineItem> GetSalesReportData()
    {
        var dataSource = @"c:\reports\June2018.xlsx";
        var data = ReportDataReader.ReadData(dataSource);

        // ... code to generate and return the report line items
    }

    // Elsewhere in the codebase we find this
    public List<ManagementReportLineItem> GetManagementReportData()
    {
        var dataSource = @"c:\reports\June2018.xlsx";
        var data = ReportDataReader.ReadData(dataSource);

        // ... code to generate and return the report line items
    }

If you forget to change one of these references to the "July2018.xslx" sheet when the new months rolls in, you will generate two reports: one from the correct data source and one from the old data source.

A solution here might be to add a method to fetch the report source and to call this new method from the two report generators.

.. code-block:: cs

    // There are still a lot of things wrong with this code overall
    // But it demonstrates the concept well enough
    private string GetReportingDataSource()
    {
        return @"c:\reports\June2018.xlsx";
    }

    public List<SalesReportLineItem> GetSalesReportData()
    {
        var dataSource = GetReportingDataSource();
        var data = ReportDataReader.ReadData(dataSource);

        // ... code to generate and return the report line items
    }

    public List<ManagementReportLineItem> GetManagementReportData()
    {
        var dataSource = GetReportingDataSource();
        var data = ReportDataReader.ReadData(dataSource);

        // ... code to generate and return the report line items
    }
