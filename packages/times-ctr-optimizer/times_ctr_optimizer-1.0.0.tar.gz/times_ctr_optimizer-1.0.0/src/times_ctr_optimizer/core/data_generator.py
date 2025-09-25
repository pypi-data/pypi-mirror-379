"""
CTR Optimization Data Generator
Professional synthetic data generation for recommendation systems
"""

import numpy as np
import pandas as pd
import polars as pl
from datetime import datetime, timedelta
from typing import Tuple, Optional
import warnings
warnings.filterwarnings('ignore')


class CTRDataGenerator:
    """
    Professional synthetic data generator for CTR optimization
    Generates realistic user events, item metadata, and contextual features
    """
    
    def __init__(self, config: Optional[dict] = None):
        """Initialize data generator with configuration"""
        self.config = config or {
            'MAX_USERS': 100000,
            'MAX_ITEMS': 50000, 
            'LOOKBACK_DAYS': 30,
            'SAMPLE_RATE': 0.1,
            'SPONSORED_RATIO': 0.15
        }
        
    def generate_user_events(self, n_users: int = 10000, n_items: int = 5000, 
                           n_events: int = 500000) -> pl.DataFrame:
        """
        Generate synthetic user interaction events with monetized items
        
        Args:
            n_users: Number of unique users
            n_items: Number of unique items
            n_events: Total number of events
            
        Returns:
            Polars DataFrame with user events
        """
        print("🚀 Generating User Event Stream...")
        np.random.seed(42)
        
        # Generate base event data
        events_data = {
            'user_id': np.random.randint(1, n_users + 1, n_events),
            'item_id': np.random.randint(1, n_items + 1, n_events),
            'timestamp': pd.date_range('2025-08-01', periods=n_events, freq='1min'),
            'session_id': np.random.randint(1, n_events // 10, n_events),
            'event_type': np.random.choice(['impression', 'click', 'add_to_cart', 'purchase'], 
                                         n_events, p=[0.7, 0.2, 0.07, 0.03]),
            'device_type': np.random.choice(['mobile', 'desktop', 'tablet'], 
                                          n_events, p=[0.6, 0.3, 0.1]),
            'ad_unit_type': np.random.choice(['banner', 'native', 'video', 'search'], 
                                           n_events, p=[0.4, 0.3, 0.2, 0.1]),
            'creative_id': np.random.randint(1, 1000, n_events),
            'position': np.random.randint(1, 21, n_events),
            'geo_country': np.random.choice(['US', 'UK', 'DE', 'FR', 'IN'], 
                                          n_events, p=[0.4, 0.2, 0.15, 0.15, 0.1]),
            'dwell_time_ms': np.random.exponential(2000, n_events).astype(int),
        }
        
        events_df = pl.DataFrame(events_data)
        
        # Add CTR label (binary click indicator)
        events_df = events_df.with_columns([
            pl.col('event_type').eq('click').cast(pl.Int8).alias('clicked'),
            pl.col('timestamp').dt.hour().alias('hour'),
            pl.col('timestamp').dt.weekday().alias('day_of_week'),
        ])
        
        print(f"✅ Generated {len(events_df):,} events for {n_users:,} users")
        return events_df
    
    def generate_item_metadata(self, n_items: int = 5000) -> pl.DataFrame:
        """
        Generate item catalog with monetization metadata
        
        Args:
            n_items: Number of items to generate
            
        Returns:
            Polars DataFrame with item metadata
        """
        print("🏷️  Generating Item Metadata...")
        np.random.seed(42)
        
        # Category hierarchy
        categories_l1 = ['Electronics', 'Fashion', 'Home', 'Sports', 'Books']
        categories_l2 = {
            'Electronics': ['Phones', 'Laptops', 'Audio', 'Gaming'],
            'Fashion': ['Clothing', 'Shoes', 'Accessories', 'Jewelry'],
            'Home': ['Furniture', 'Kitchen', 'Decor', 'Garden'],
            'Sports': ['Fitness', 'Outdoor', 'Team Sports', 'Water Sports'],
            'Books': ['Fiction', 'Non-fiction', 'Educational', 'Comics']
        }
        
        items_data = {
            'item_id': range(1, n_items + 1),
            'price': np.random.lognormal(3, 1, n_items).round(2),
            'margin_pct': np.random.uniform(10, 50, n_items).round(1),
            'brand_id': np.random.randint(1, 500, n_items),
            'is_sponsored': np.random.choice([0, 1], n_items, 
                                           p=[1-self.config['SPONSORED_RATIO'], 
                                             self.config['SPONSORED_RATIO']]),
            'cpc_bid': np.random.uniform(0.1, 2.0, n_items).round(3),
            'quality_score': np.random.uniform(1, 10, n_items).round(2),
            'inventory_count': np.random.randint(0, 1000, n_items),
            'created_date': pd.date_range('2024-01-01', periods=n_items, freq='1H'),
        }
        
        # Generate category assignments
        cat_l1 = np.random.choice(categories_l1, n_items)
        cat_l2 = [np.random.choice(categories_l2[c]) for c in cat_l1]
        
        items_data['category_l1'] = cat_l1
        items_data['category_l2'] = cat_l2
        
        # Generate synthetic text features
        titles = [f"Premium {cat_l2[i]} Item {items_data['item_id'][i]}" 
                 for i in range(n_items)]
        descriptions = [f"High-quality {cat_l1[i]} product with excellent features" 
                       for i in range(n_items)]
        
        items_data['title'] = titles
        items_data['description'] = descriptions
        
        items_df = pl.DataFrame(items_data)
        
        # Calculate derived fields
        items_df = items_df.with_columns([
            (pl.col('price') * pl.col('margin_pct') / 100).round(2).alias('margin_amount'),
            (pl.col('cpc_bid') * pl.col('is_sponsored')).round(3).alias('payout'),
            pl.when(pl.col('inventory_count') == 0).then(1).otherwise(0).alias('is_out_of_stock')
        ])
        
        sponsored_count = items_df['is_sponsored'].sum()
        print(f"✅ Generated metadata for {len(items_df):,} items")
        print(f"   - {sponsored_count:,} sponsored items ({sponsored_count/len(items_df)*100:.1f}%)")
        
        return items_df
    
    def generate_context_features(self, events_df: pl.DataFrame) -> pl.DataFrame:
        """
        Add contextual features to events
        
        Args:
            events_df: Base events DataFrame
            
        Returns:
            Events DataFrame with contextual features
        """
        print("🌐 Adding Contextual Features...")
        
        # Campaign and budget context
        campaign_data = pl.DataFrame({
            'ad_unit_type': ['banner', 'native', 'video', 'search'],
            'daily_budget': [10000, 15000, 25000, 8000],
            'current_spend': [3000, 7500, 12000, 2000],
            'target_ctr': [0.02, 0.035, 0.045, 0.05]
        })
        
        # Join context to events
        events_with_context = events_df.join(campaign_data, on='ad_unit_type', how='left')
        
        # Add time-based features
        events_with_context = events_with_context.with_columns([
            pl.col('timestamp').dt.month().alias('month'),
            pl.col('hour').is_between(9, 17).alias('is_business_hours'),
            pl.col('day_of_week').is_in([6, 7]).alias('is_weekend'),
            (pl.col('current_spend') / pl.col('daily_budget')).alias('budget_utilization')
        ])
        
        print("✅ Added contextual features")
        return events_with_context
        
    def generate_complete_dataset(self, n_users: int = 100000, n_items: int = 50000, 
                                n_events: int = 1000000) -> Tuple[pl.DataFrame, pl.DataFrame]:
        """
        Generate complete synthetic dataset for CTR optimization
        
        Args:
            n_users: Number of users
            n_items: Number of items  
            n_events: Number of events
            
        Returns:
            Tuple of (events_df, items_df)
        """
        print("🚀 CTR Optimization Pipeline - Raw Data Sources")
        print("=" * 60)
        print()
        print("🔄 Starting Data Ingestion Pipeline...")
        
        # Generate core data
        events_df = self.generate_user_events(n_users, n_items, n_events)
        items_df = self.generate_item_metadata(n_items)
        
        # Add context
        events_df = self.generate_context_features(events_df)
        
        # Validation
        print()
        print("🔍 Data Validation:")
        print(f"Events shape: {events_df.shape}")
        print(f"Items shape: {items_df.shape}")
        print(f"Memory usage: {(events_df.estimated_size() + items_df.estimated_size()) / 1024**2:.1f} MB")
        print(f"CTR: {events_df['clicked'].mean():.3f}")
        
        # Calculate sponsored impression ratio
        events_with_items = events_df.join(items_df, on='item_id')
        sponsored_ratio = events_with_items['is_sponsored'].mean()
        print(f"Sponsored impression ratio: {sponsored_ratio:.3f}")
        
        return events_df, items_df


# Factory function for easy import
def create_data_generator(config: Optional[dict] = None) -> CTRDataGenerator:
    """Factory function to create CTR data generator"""
    return CTRDataGenerator(config)
