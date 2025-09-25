import pytest
import numpy as np
import pandas as pd
from unittest.mock import Mock, patch
import matplotlib.pyplot as plt

from marci.campaigns import Campaign
from marci.utils.portfolio import Portfolio


class TestPortfolio:
    """Test suite for the Portfolio class."""

    @pytest.fixture
    def sample_campaigns(self):
        """Create sample campaigns for testing."""
        campaigns = [
            Campaign(
                name="Paid Campaign 1",
                cpm=10.0,
                cvr=0.05,
                aov=100.0,
                cv=0.2,
                start_date="2024-01-01",
                duration=30,
                base_budget=1000.0,
                is_organic=False,
            ),
            Campaign(
                name="Paid Campaign 2",
                cpm=15.0,
                cvr=0.03,
                aov=150.0,
                cv=0.25,
                start_date="2024-01-01",
                duration=30,
                base_budget=1500.0,
                is_organic=False,
            ),
            Campaign(
                name="Organic Campaign",
                cpm=0.0,
                cvr=0.02,
                aov=80.0,
                cv=0.15,
                start_date="2024-01-01",
                duration=30,
                base_budget=0.0,
                is_organic=True,
            ),
        ]
        return campaigns

    @pytest.fixture
    def portfolio(self, sample_campaigns):
        """Create a portfolio instance for testing."""
        return Portfolio(sample_campaigns)

    def test_portfolio_initialization(self, sample_campaigns):
        """Test portfolio initialization."""
        portfolio = Portfolio(sample_campaigns)
        
        # Check campaigns dictionary
        assert len(portfolio.campaigns) == 3
        assert "Paid Campaign 1" in portfolio.campaigns
        assert "Paid Campaign 2" in portfolio.campaigns
        assert "Organic Campaign" in portfolio.campaigns
        
        # Check names list
        assert len(portfolio.names) == 3
        assert "Paid Campaign 1" in portfolio.names
        
        # Check organic campaigns
        assert len(portfolio.organic_campaigns) == 1
        assert portfolio.organic_campaigns[0].name == "Organic Campaign"
        assert len(portfolio.organic_names) == 1
        assert "Organic Campaign" in portfolio.organic_names
        
        # Check paid campaigns
        assert len(portfolio.paid_campaigns) == 2
        paid_names = [c.name for c in portfolio.paid_campaigns]
        assert "Paid Campaign 1" in paid_names
        assert "Paid Campaign 2" in paid_names
        assert len(portfolio.paid_names) == 2
        
        # Check initial df is None
        assert portfolio.df is None

    def test_portfolio_color_assignment(self, sample_campaigns):
        """Test that colors are assigned to campaigns without colors."""
        # Create campaigns without colors
        campaigns_no_color = [
            Campaign(
                name="Campaign 1",
                cpm=10.0,
                cvr=0.05,
                aov=100.0,
                cv=0.2,
                start_date="2024-01-01",
                duration=30,
                base_budget=1000.0,
                is_organic=False,
            ),
            Campaign(
                name="Campaign 2",
                cpm=15.0,
                cvr=0.03,
                aov=150.0,
                cv=0.25,
                start_date="2024-01-01",
                duration=30,
                base_budget=1500.0,
                is_organic=False,
                color="#FF0000",  # Pre-assigned color
            ),
        ]
        
        portfolio = Portfolio(campaigns_no_color)
        
        # Check that color was assigned to campaign without color
        assert portfolio.campaigns["Campaign 1"].color is not None
        assert portfolio.campaigns["Campaign 2"].color == "#FF0000"

    def test_exp_paid_sales(self, portfolio):
        """Test expected paid sales calculation."""
        budgets = np.array([1200.0, 1800.0])
        
        # Mock the exp_daily_sales method for paid campaigns
        with patch.object(portfolio.paid_campaigns[0], 'exp_daily_sales', return_value=100.0) as mock1, \
             patch.object(portfolio.paid_campaigns[1], 'exp_daily_sales', return_value=150.0) as mock2:
            
            result = portfolio.exp_paid_sales(budgets)
            
            assert result == 250.0
            mock1.assert_called_once_with(1200.0)
            mock2.assert_called_once_with(1800.0)

    def test_exp_paid_sales_empty_paid_campaigns(self):
        """Test exp_paid_sales with no paid campaigns."""
        # Create portfolio with only organic campaigns
        organic_campaign = Campaign(
            name="Organic Campaign",
            cpm=0.0,
            cvr=0.02,
            aov=80.0,
            cv=0.15,
            start_date="2024-01-01",
            duration=30,
            base_budget=0.0,
            is_organic=True,
        )
        portfolio = Portfolio([organic_campaign])
        
        result = portfolio.exp_paid_sales(np.array([]))
        assert result == 0.0

    def test_find_optimal_budgets(self, portfolio):
        """Test optimal budget allocation."""
        total_budget = 2000.0
        
        # Mock the exp_daily_sales method to return predictable values
        with patch.object(portfolio.paid_campaigns[0], 'exp_daily_sales', return_value=100.0) as mock1, \
             patch.object(portfolio.paid_campaigns[1], 'exp_daily_sales', return_value=150.0) as mock2:
            
            result = portfolio.find_optimal_budgets(total_budget)
            
            # Check that result is a dictionary
            assert isinstance(result, dict)
            assert len(result) == 2
            assert "Paid Campaign 1" in result
            assert "Paid Campaign 2" in result
            
            # Check that budgets sum to total budget
            total_allocated = sum(result.values())
            assert abs(total_allocated - total_budget) < 1e-6
            
            # Check that all budgets are non-negative
            for budget in result.values():
                assert budget >= 0

    def test_find_optimal_budgets_no_paid_campaigns(self):
        """Test optimal budget allocation with no paid campaigns."""
        organic_campaign = Campaign(
            name="Organic Campaign",
            cpm=0.0,
            cvr=0.02,
            aov=80.0,
            cv=0.15,
            start_date="2024-01-01",
            duration=30,
            base_budget=0.0,
            is_organic=True,
        )
        portfolio = Portfolio([organic_campaign])
        
        # This should raise an error or return empty dict
        with pytest.raises(ValueError):
            portfolio.find_optimal_budgets(1000.0)

    def test_sim_outcomes(self, portfolio):
        """Test simulation outcomes."""
        budgets = {
            "Paid Campaign 1": 1200.0,
            "Paid Campaign 2": 1800.0,
            "Organic Campaign": 0.0,
        }
        
        # Mock the sim_outcomes method for campaigns
        mock_dfs = [
            pd.DataFrame({"date": ["2024-01-01"], "sales": [100.0], "budget": [1200.0]}),
            pd.DataFrame({"date": ["2024-01-01"], "sales": [150.0], "budget": [1800.0]}),
            pd.DataFrame({"date": ["2024-01-01"], "sales": [50.0], "budget": [0.0]}),
        ]
        
        with patch.object(portfolio.campaigns["Paid Campaign 1"], 'sim_outcomes') as mock1, \
             patch.object(portfolio.campaigns["Paid Campaign 2"], 'sim_outcomes') as mock2, \
             patch.object(portfolio.campaigns["Organic Campaign"], 'sim_outcomes') as mock3:
            
            # Set up the df attribute for each campaign
            portfolio.campaigns["Paid Campaign 1"].df = mock_dfs[0]
            portfolio.campaigns["Paid Campaign 2"].df = mock_dfs[1]
            portfolio.campaigns["Organic Campaign"].df = mock_dfs[2]
            
            result = portfolio.sim_outcomes(budgets)
            
            # Check that sim_outcomes was called with correct budgets
            mock1.assert_called_once_with(budget=1200.0)
            mock2.assert_called_once_with(budget=1800.0)
            mock3.assert_called_once_with(budget=0.0)
            
            # Check result is a DataFrame
            assert isinstance(result, pd.DataFrame)
            assert len(result) == 3  # 3 rows from 3 campaigns
            
            # Check that portfolio.df was set
            assert portfolio.df is not None

    def test_sim_outcomes_default_budgets(self, portfolio):
        """Test simulation outcomes with default budgets."""
        # Mock the sim_outcomes method
        with patch.object(portfolio.campaigns["Paid Campaign 1"], 'sim_outcomes') as mock1, \
             patch.object(portfolio.campaigns["Paid Campaign 2"], 'sim_outcomes') as mock2, \
             patch.object(portfolio.campaigns["Organic Campaign"], 'sim_outcomes') as mock3:
            
            # Set up the df attribute for each campaign
            portfolio.campaigns["Paid Campaign 1"].df = pd.DataFrame({"date": ["2024-01-01"], "sales": [100.0]})
            portfolio.campaigns["Paid Campaign 2"].df = pd.DataFrame({"date": ["2024-01-01"], "sales": [150.0]})
            portfolio.campaigns["Organic Campaign"].df = pd.DataFrame({"date": ["2024-01-01"], "sales": [50.0]})
            
            result = portfolio.sim_outcomes()
            
            # Check that sim_outcomes was called with base budgets
            mock1.assert_called_once_with(budget=1000.0)
            mock2.assert_called_once_with(budget=1500.0)
            mock3.assert_called_once_with(budget=0.0)

    @patch('matplotlib.pyplot.show')
    def test_plot(self, mock_show, portfolio):
        """Test portfolio plotting functionality."""
        # Create a sample DataFrame with proper index
        sample_df = pd.DataFrame({
            'name': ['Paid Campaign 1', 'Paid Campaign 2'],
            'budget': [1000.0, 1500.0],
            'sales': [100.0, 150.0]
        })
        sample_df.index = ['2024-01-01', '2024-01-02']
        
        # Mock the pivot_table method
        with patch.object(sample_df, 'pivot_table') as mock_pivot:
            mock_pivot.return_value = pd.DataFrame({
                'Paid Campaign 1': [1000.0, 1000.0],
                'Paid Campaign 2': [1500.0, 1500.0]
            }, index=['2024-01-01', '2024-01-02'])
            
            # Mock the style function
            with patch('marci.utils.portfolio.style') as mock_style:
                portfolio.plot(sample_df)
                
                # Check that show was called
                mock_show.assert_called_once()
                
                # Check that style was called twice (for both subplots)
                assert mock_style.call_count == 2

    @patch('matplotlib.pyplot.show')
    def test_plot_with_default_df(self, mock_show, portfolio):
        """Test portfolio plotting with default DataFrame."""
        # Set up portfolio.df with proper index
        sample_df = pd.DataFrame({
            'name': ['Paid Campaign 1'],
            'budget': [1000.0],
            'sales': [100.0]
        })
        sample_df.index = ['2024-01-01']
        portfolio.df = sample_df
        
        # Mock the pivot_table method
        with patch.object(sample_df, 'pivot_table') as mock_pivot:
            mock_pivot.return_value = pd.DataFrame({
                'Paid Campaign 1': [1000.0]
            }, index=['2024-01-01'])
            
            # Mock the style function
            with patch('marci.utils.portfolio.style') as mock_style:
                portfolio.plot()
                
                # Check that show was called
                mock_show.assert_called_once()

    def test_print_stats(self, portfolio, capsys):
        """Test print_stats method."""
        budgets = {
            "Paid Campaign 1": 1200.0,
            "Paid Campaign 2": 1800.0,
        }
        
        # Mock the exp_daily_sales and exp_roas methods for paid campaigns
        with patch.object(portfolio.paid_campaigns[0], 'exp_daily_sales', return_value=100.0) as mock1, \
             patch.object(portfolio.paid_campaigns[1], 'exp_daily_sales', return_value=150.0) as mock2, \
             patch.object(portfolio.paid_campaigns[0], 'exp_roas', return_value=2.0) as mock3, \
             patch.object(portfolio.paid_campaigns[1], 'exp_roas', return_value=1.5) as mock4, \
             patch.object(portfolio.organic_campaigns[0], 'exp_daily_sales', return_value=50.0) as mock5:
            
            portfolio.print_stats(budgets)
            
            # Capture the printed output
            captured = capsys.readouterr()
            output = captured.out
            
            # Check that output contains expected columns
            assert "base_budget" in output
            assert "base_sales" in output
            assert "base_roas" in output
            assert "budget" in output
            assert "elasticity" in output
            assert "exp_roas" in output
            assert "exp_sales" in output
            
            # Check that campaign names are in output
            assert "Paid Campaign 1" in output
            assert "Paid Campaign 2" in output
            assert "Organic Campaign" in output

    def test_print_stats_default_budgets(self, portfolio, capsys):
        """Test print_stats with default budgets."""
        # Mock the exp_daily_sales and exp_roas methods
        with patch.object(portfolio.paid_campaigns[0], 'exp_daily_sales', return_value=100.0) as mock1, \
             patch.object(portfolio.paid_campaigns[1], 'exp_daily_sales', return_value=150.0) as mock2, \
             patch.object(portfolio.paid_campaigns[0], 'exp_roas', return_value=2.0) as mock3, \
             patch.object(portfolio.paid_campaigns[1], 'exp_roas', return_value=1.5) as mock4, \
             patch.object(portfolio.organic_campaigns[0], 'exp_daily_sales', return_value=50.0) as mock5:
            
            portfolio.print_stats()
            
            # Capture the printed output
            captured = capsys.readouterr()
            output = captured.out
            
            # Check that output contains expected content
            assert "base_budget" in output
            assert "Paid Campaign 1" in output
            assert "Paid Campaign 2" in output

    def test_portfolio_edge_cases(self):
        """Test portfolio with edge cases."""
        # Test with empty campaigns list
        empty_portfolio = Portfolio([])
        assert len(empty_portfolio.campaigns) == 0
        assert len(empty_portfolio.names) == 0
        assert len(empty_portfolio.organic_campaigns) == 0
        assert len(empty_portfolio.paid_campaigns) == 0
        
        # Test exp_paid_sales with empty portfolio
        result = empty_portfolio.exp_paid_sales(np.array([]))
        assert result == 0.0
        
        # Test find_optimal_budgets with empty portfolio should raise error
        with pytest.raises(ValueError):
            empty_portfolio.find_optimal_budgets(1000.0)

    def test_portfolio_campaign_access(self, portfolio):
        """Test accessing campaigns through the portfolio."""
        # Test accessing campaigns by name
        campaign1 = portfolio.campaigns["Paid Campaign 1"]
        assert campaign1.name == "Paid Campaign 1"
        assert not campaign1.is_organic
        
        campaign2 = portfolio.campaigns["Paid Campaign 2"]
        assert campaign2.name == "Paid Campaign 2"
        assert not campaign2.is_organic
        
        organic_campaign = portfolio.campaigns["Organic Campaign"]
        assert organic_campaign.name == "Organic Campaign"
        assert organic_campaign.is_organic

    def test_portfolio_campaign_lists(self, portfolio):
        """Test campaign list properties."""
        # Test names list
        assert len(portfolio.names) == 3
        assert "Paid Campaign 1" in portfolio.names
        assert "Paid Campaign 2" in portfolio.names
        assert "Organic Campaign" in portfolio.names
        
        # Test organic names
        assert len(portfolio.organic_names) == 1
        assert "Organic Campaign" in portfolio.organic_names
        
        # Test paid names
        assert len(portfolio.paid_names) == 2
        assert "Paid Campaign 1" in portfolio.paid_names
        assert "Paid Campaign 2" in portfolio.paid_names
        assert "Organic Campaign" not in portfolio.paid_names
